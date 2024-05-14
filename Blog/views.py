from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from Blog.models import Blog


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog/blog_form.html'
    fields = ('title', 'body', 'preview', 'date_of_creation',)
    success_url = reverse_lazy('Blog:list')
    permission_required = 'Blog.add_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = self.request.user
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': " Блог",
    }

    template_name = 'Blog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'Blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'date_of_creation',)
    success_url = reverse_lazy('Blog:list')
    permission_required = 'Blog.update_blog'

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('Blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'Blog/blog_confirm_delete.html'
    success_url = reverse_lazy('Blog:list')
    permission_required = 'Blog.delete_blog'

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author


def toogle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True
    blog_item.save()
    return redirect('Blog:list')
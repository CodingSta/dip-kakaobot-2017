from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_length', 'status', 'created_at']
    list_display_links = ['title']
    list_filter = ['status', 'updated_at']
    search_fields = ['title']
    actions = ['make_published', 'make_unpublished']

    def get_length(self, post):
        html = '<strong>{}</strong>'.format(len(post.conent))
        return mark_safe(html)
    get_length.short_description = '글자 수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request,
            '{}개를 발행했소.'.format(updated_count))
    make_published.short_description = '선택한 글 발행하기'

    def make_unpublished(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request,
            '{}개를 발행 취소했소.'.format(updated_count))
    make_unpublished.short_description = '선택한 글 발행 취소하기'

# admin.site.register(Post, PostAdmin)

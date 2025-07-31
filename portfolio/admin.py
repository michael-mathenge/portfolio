from django.contrib import admin
from .models import (
    HeroSection, SocialLink, AboutSection, Skill, ResumeItem, 
    Service, Testimonial, ContactInfo
)

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'period')
    list_filter = ('category',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'author_title', 'rating')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'whatsapp_number')
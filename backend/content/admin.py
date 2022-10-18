from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.urls import path
from parler.admin import TranslatableAdmin

from content.models import Blog, HomePage
from django.conf import settings
from .api import get_locale, get_homepage_collection


class BlogAdmin(TranslatableAdmin):
    list_display = ('title',)
    search_fields = ('translations__title', 'translations__content')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


class CustomHomeAdmin(admin.ModelAdmin):
    actions = None

    # these are only for flat fields (nested image fields are processed separately)
    image_fields = [
        'button_icon',
        'footerIcon',
        'imageBg',
        'icon_100',
        'icon66',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if not self.model.objects.count() == 1:
                self.model.objects.all().delete()
                self.model.objects.create()
        except:
            pass

    def has_add_permission(self, request):
        return False

    def get_urls(self):
        return [path('home', self.home_page, name='home')] + super().get_urls()

    def home_page(self, request):
        images_dir = '/images/'

        if request.method == 'POST':
            main_block_data = {
                'title_top': request.POST.get('main_block__title_top', ''),
                'title_h2': request.POST.get('main_block__title_h2', ''),
                'title_h2_color': request.POST.get('main_block__title_h2_color', ''),
                'title_h2_price': request.POST.get('main_block__title_h2_price', ''),
                'title_button': request.POST.get('main_block__title_button', ''),
                'button_title': request.POST.get('main_block__button_title', ''),
                'button_icon': request.POST.get('main_block__button_icon', ''),
                'footerTitle': request.POST.get('main_block__footerTitle', ''),
                'footerTitleTwo': request.POST.get('main_block__footerTitleTwo', ''),
                'footerIcon': request.POST.get('main_block__footerIcon', ''),
                'imageBg': request.POST.get('main_block__imageBg', ''),
            }

            block_two_data = {
                'imageBg': request.POST.get('block_two__imageBg', ''),
                'titleH2': request.POST.get('block_two__titleH2', ''),
                'cards': [
                    {
                        'id': '1',
                        'icon': request.POST.get('block_two__card_1_icon', ''),
                        'title': request.POST.get('block_two__card_1_title', ''),
                        'sub_title': request.POST.get('block_two__card_1_sub_title', ''),
                    },

                    {
                        'id': '2',
                        'icon': request.POST.get('block_two__card_2_icon', ''),
                        'title': request.POST.get('block_two__card_2_title', ''),
                        'sub_title': request.POST.get('block_two__card_2_sub_title', ''),
                    },

                    {
                        'id': '3',
                        'icon': request.POST.get('block_two__card_3_icon', ''),
                        'title': request.POST.get('block_two__card_3_title', ''),
                        'sub_title': request.POST.get('block_two__card_3_sub_title', ''),
                    },

                    {

                        'id': '4',
                        'icon': request.POST.get('block_two__card_4_icon', ''),
                        'title': request.POST.get('block_two__card_4_title', ''),
                        'sub_title': request.POST.get('block_two__card_4_sub_title', ''),
                    },
                ],
            }

            block_three_data = {
                'imageBg': request.POST.get('block_three__imageBg', ''),
                'icon_100': request.POST.get('block_three__icon_100', ''),
                'icon_100_title': request.POST.get('block_three__icon_100_title', ''),
                'title_h2': request.POST.get('block_three__title_h2', ''),
                'subtitle': request.POST.get('block_three__subtitle', ''),
            }

            # block 7 minutes has several pages
            block_seven_index_data = {
                'title_h2': request.POST.get('block_seven_index__title_h2', ''),
            }

            block_seven_stats_data = {
                'cards': [
                    {
                        'id': '1',
                        'reviews': request.POST.get('block_seven_stats__card_1_reviews', ''),
                        'title': request.POST.get('block_seven_stats__card_1_title', ''),
                        'followers': request.POST.get('block_seven_stats__card_1_followers', ''),
                        'icon': request.POST.get('block_seven_stats__card_1_icon', ''),
                        'link': request.POST.get('block_seven_stats__card_1_link', ''),
                    },
                    {
                        'id': '2',
                        'reviews': request.POST.get('block_seven_stats__card_2_reviews', ''),
                        'title': request.POST.get('block_seven_stats__card_2_title', ''),
                        'followers': request.POST.get('block_seven_stats__card_2_followers', ''),
                        'icon': request.POST.get('block_seven_stats__card_2_icon', ''),
                        'link': request.POST.get('block_seven_stats__card_2_link', ''),
                    },
                    {
                        'id': '3',
                        'reviews': request.POST.get('block_seven_stats__card_3_reviews', ''),
                        'title': request.POST.get('block_seven_stats__card_3_title', ''),
                        'followers': request.POST.get('block_seven_stats__card_3_followers', ''),
                        'icon': request.POST.get('block_seven_stats__card_3_icon', ''),
                        'link': request.POST.get('block_seven_stats__card_3_link', ''),
                    },
                ],

                'button': {
                    'title': request.POST.get('block_seven_stats__button_title', ''),
                    'icon': request.POST.get('block_seven_stats__button_icon', ''),
                }
            }

            block_seven_recready_data = {
                'recommend_text': request.POST.get('block_seven_recready__recommend_text', ''),
            }

            block_seven_recblog_data = {
                'imageBg': request.POST.get('block_seven_recblog__imageBg', ''),
                'recommend_text': {
                    'title': request.POST.get('block_seven_recblog__rectext_title', ''),
                    'link': request.POST.get('block_seven_recblog__rectext_link', ''),
                    'title_next': request.POST.get('block_seven_recblog__rectext_title_next', ''),
                }
            }

            block_seven_jurist_data = {
                'imageBg': request.POST.get('block_seven_jurist__imageBg', ''),
                'icon66': request.POST.get('block_seven_jurist__icon66', ''),
                'slogan': {
                    'title': request.POST.get('block_seven_jurist__slogan_title', ''),
                    'jurist': request.POST.get('block_seven_jurist__slogan_jurist', ''),
                    'link_title': request.POST.get('block_seven_jurist__slogan_link_title', ''),
                    'link': request.POST.get('block_seven_jurist__slogan_link', ''),
                },
            }

            block_seven_createapp_data = {
                'link_text': request.POST.get('block_seven_createapp__link_text', ''),
                'cards': [
                    {
                        'id': '1',
                        'icon': request.POST.get('block_seven_createapp__card_1_icon', ''),
                        'title': request.POST.get('block_seven_createapp__card_1_title', ''),
                    },
                    {
                        'id': '2',
                        'icon': request.POST.get('block_seven_createapp__card_2_icon', ''),
                        'title': request.POST.get('block_seven_createapp__card_2_title', ''),
                    },
                    {
                        'id': '3',
                        'icon': request.POST.get('block_seven_createapp__card_3_icon', ''),
                        'title': request.POST.get('block_seven_createapp__card_3_title', ''),
                    },
                    {
                        'id': '4',
                        'icon': request.POST.get('block_seven_createapp__card_4_icon', ''),
                        'title': request.POST.get('block_seven_createapp__card_4_title', ''),
                    },
                ],

                'button': {
                    'title': request.POST.get('block_seven_createapp__button_title', ''),
                    'icon': request.POST.get('block_seven_createapp__button_icon', ''),
                    'link': request.POST.get('block_seven_createapp__button_link', ''),
                }
            }

            block_review_index_data = {
                'blockReview_title': request.POST.get('block_review_index__blockReview_title', ''),
                'buttonLink': {
                    'title': request.POST.get('block_review_index__button_title', ''),
                    'icon': request.POST.get('block_review_index__button_icon', ''),
                    'link': request.POST.get('block_review_index__button_link', ''),
                }
            }

            block_review_slide_data = {
                'reviews': [
                    {
                        'id': 1,
                        'name': request.POST.get('block_review_slide__rev_1_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_1_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_1_text', ''),
                    },
                    {
                        'id': 2,
                        'name': request.POST.get('block_review_slide__rev_2_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_2_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_2_text', ''),
                    },
                    {
                        'id': 3,
                        'name': request.POST.get('block_review_slide__rev_3_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_3_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_3_text', ''),
                    },
                    {
                        'id': 4,
                        'name': request.POST.get('block_review_slide__rev_4_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_4_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_4_text', ''),
                    },
                    {
                        'id': 5,
                        'name': request.POST.get('block_review_slide__rev_5_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_5_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_5_text', ''),
                    },
                    {
                        'id': 6,
                        'name': request.POST.get('block_review_slide__rev_6_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_6_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_6_text', ''),
                    },
                    {
                        'id': 7,
                        'name': request.POST.get('block_review_slide__rev_7_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_7_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_7_text', ''),
                    },
                    {
                        'id': 8,
                        'name': request.POST.get('block_review_slide__rev_8_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_8_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_8_text', ''),
                    },
                    {
                        'id': 9,
                        'name': request.POST.get('block_review_slide__rev_9_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_9_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_9_text', ''),
                    },
                    {
                        'id': 10,
                        'name': request.POST.get('block_review_slide__rev_10_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_10_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_10_text', ''),
                    },
                    {
                        'id': 11,
                        'name': request.POST.get('block_review_slide__rev_11_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_11_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_11_text', ''),
                    },
                    {
                        'id': 12,
                        'name': request.POST.get('block_review_slide__rev_12_name', ''),
                        'avatar': request.POST.get('block_review_slide__rev_12_avatar', ''),
                        'review_text': request.POST.get('block_review_slide__rev_12_text', ''),
                    },
                ]
            }

            block_review_review_data = {
                'icon66': request.POST.get('block_review_review__icon66', ''),
            }

            block_faq_data = {
                'blockFAQ_title': request.POST.get('block_faq__blockFAQ_title', ''),
                'questions': [
                    {
                        'id': '1',
                        'question': request.POST.get('block_faq__q_1_question', ''),
                        'answer': request.POST.get('block_faq__q_1_answer', ''),
                    },
                    {
                        'id': '2',
                        'question': request.POST.get('block_faq__q_2_question', ''),
                        'answer': request.POST.get('block_faq__q_2_answer', ''),
                    },
                    {
                        'id': '3',
                        'question': request.POST.get('block_faq__q_3_question', ''),
                        'answer': request.POST.get('block_faq__q_3_answer', ''),
                    },
                    {
                        'id': '4',
                        'question': request.POST.get('block_faq__q_4_question', ''),
                        'answer': request.POST.get('block_faq__q_4_answer', ''),
                    },
                    {
                        'id': '5',
                        'question': request.POST.get('block_faq__q_5_question', ''),
                        'answer': request.POST.get('block_faq__q_5_answer', ''),
                    },
                    {
                        'id': '6',
                        'question': request.POST.get('block_faq__q_6_question', ''),
                        'answer': request.POST.get('block_faq__q_6_answer', ''),
                    },
                    {
                        'id': '7',
                        'question': request.POST.get('block_faq__q_7_question', ''),
                        'answer': request.POST.get('block_faq__q_7_answer', ''),
                    },
                    {
                        'id': '8',
                        'question': request.POST.get('block_faq__q_8_question', ''),
                        'answer': request.POST.get('block_faq__q_8_answer', ''),
                    },

                ],
                'icon_arrow': {
                    'up': request.POST.get('block_faq__icon_arrow_up', ''),
                    'down': request.POST.get('block_faq__icon_arrow_down', ''),
                }

            }

            # for images in nested fields (custom structures)
            files_to_del = []

            for name in request.FILES:
                if name.startswith('block_two__card_') and name.endswith('_icon'):
                    i = int(name.split('_')[4])
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_two_data['cards'][i - 1].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name.startswith('block_seven_stats__card_') and name.endswith('_icon'):
                    i = int(name.split('_')[5])
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_seven_stats_data['cards'][i - 1].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name == 'block_seven_stats__button_icon':
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_seven_stats_data['button'].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name.startswith('block_seven_createapp__card_') and name.endswith('_icon'):
                    i = int(name.split('_')[5])
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_seven_createapp_data['cards'][i - 1].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name == 'block_seven_createapp__button_icon':
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_seven_createapp_data['button'].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name == 'block_review_index__button_icon':
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_review_index_data['buttonLink'].update({'icon': images_dir + filename})

            for name in request.FILES:
                if name == 'block_faq__icon_arrow_up':
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_faq_data['icon_arrow'].update({'up': images_dir + filename})

            for name in request.FILES:
                if name == 'block_faq__icon_arrow_down':
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_faq_data['icon_arrow'].update({'down': images_dir + filename})

            for name in request.FILES:
                if name.startswith('block_review_slide__rev') and name.endswith('_avatar'):
                    i = int(name.split('_')[5])
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    files_to_del.append(name)
                    block_review_slide_data['reviews'][i - 1].update({'avatar': images_dir + filename})

            # delete saved files from request before processing all other image fields
            for name in files_to_del:
                del request.FILES[name]

            # all other images (flat fields)
            for name in request.FILES:
                block_name, field_name = name.split('__')
                if field_name in self.image_fields:
                    file = request.FILES[name]
                    fs = FileSystemStorage(settings.MEDIA_ROOT + images_dir)
                    filename = fs.save(file.name, file)
                    dict_name = block_name + '_data'
                    locals()[dict_name].update({field_name: images_dir + filename})

            # save data from data dicts to the db
            data_dict_names = [d for d in locals() if d.endswith('_data')]
            for name in data_dict_names:
                get_homepage_collection(request).update_one({'_id': name[:-5]}, {'$set': locals()[name]}, upsert=True)

        context = {
            **self.admin_site.each_context(request),
            'content': {doc['_id']: doc for doc in get_homepage_collection(request).find()},
            'image_fields': self.image_fields,
            'locale': get_locale(request),
        }
        return render(request, 'admin/home.html', context=context)


admin.site.register(Blog, BlogAdmin)
admin.site.register(HomePage, CustomHomeAdmin)

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    RichTextFieldPanel,
)

class BasicPage(Page):

    body = StreamField([
        ('rich_text', RichTextBlock())
    ])
    second_body = RichTextField(blank=True)

    # show in menu ticked by default
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        RichTextFieldPanel('second_body')
    ]

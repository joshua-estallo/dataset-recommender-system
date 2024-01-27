from django import forms
from .models import Dataset
from django_select2.forms import Select2MultipleWidget, Select2Widget
from django.forms.widgets import DateInput


CATEGORY_CHOICES = (
    ('Accounting', 'Accounting'),
    ('Administration', 'Administration'),
    ('Advertising', 'Advertising'),
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Architecture', 'Architecture'),
    ('Arts and Entertainment', 'Arts and Entertainment'),
    ('Automotive', 'Automotive'),
    ('Aviation', 'Aviation'),
    ('Banking', 'Banking'),
    ('Biotechnology', 'Biotechnology'),
    ('Business Development', 'Business Development'),
    ('Business Services', 'Business Services'),
    ('Chemicals', 'Chemicals'),
    ('Clean Energy', 'Clean Energy'),
    ('Computer Hardware', 'Computer Hardware'),
    ('Computer Software', 'Computer Software'),
    ('Construction', 'Construction'),
    ('Consulting', 'Consulting'),
    ('Consumer Goods', 'Consumer Goods'),
    ('Defense', 'Defense'),
    ('Design', 'Design'),
    ('Education', 'Education'),
    ('Electronics', 'Electronics'),
    ('Energy', 'Energy'),
    ('Engineering', 'Engineering'),
    ('Environmental Services', 'Environmental Services'),
    ('Finance', 'Finance'),
    ('Food and Beverage', 'Food and Beverage'),
    ('Forestry', 'Forestry'),
    ('Government', 'Government'),
    ('Healthcare', 'Healthcare'),
    ('Hospitality', 'Hospitality'),
    ('Human Resources', 'Human Resources'),
    ('Information Technology', 'Information Technology'),
    ('Insurance', 'Insurance'),
    ('Legal', 'Legal'),
    ('Logistics', 'Logistics'),
    ('Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ('Media', 'Media'),
    ('Medical', 'Medical'),
    ('Mining', 'Mining'),
    ('Nonprofit', 'Nonprofit'),
    ('Oil and Gas', 'Oil and Gas'),
    ('Pharmaceuticals', 'Pharmaceuticals'),
    ('Professional Services', 'Professional Services'),
    ('Real Estate', 'Real Estate'),
    ('Retail', 'Retail'),
    ('Sales', 'Sales'),
    ('Science and Engineering', 'Science and Engineering'),
    ('Sports', 'Sports'),
    ('Technology', 'Technology'),
    ('Telecommunications', 'Telecommunications'),
    ('Transportation', 'Transportation'),
    ('Travel and Tourism', 'Travel and Tourism'),
    ('Utilities', 'Utilities'),
    ('Wholesale', 'Wholesale'),
    ('Other', 'Other'),
)

DATA_TYPE_CHOICES = (
    ("Audio", "Audio"),
    # ("Bigquery", "Bigquery"),
    # ("Categorical", "Categorical"),
    # ("Graph", "Graph"),
    ("Image", "Image"),
    # ("Multimodal", "Multimodal"),
    ("Tabular", "Tabular"),
    ("Text", "Text"),
    # ("Video", "Video"),
)

FILE_FORMAT_CHOICES = (
    # Audio
    ("wav", "WAV"),
    ("mp3", "MP3"),
    ("flac", "FLAC (Lossless)"),
    ("ogg", "OGG (Vorbis)"),
    ("m4a", "M4A (AAC)"),
    ("aiff", "AIFF"),
    ("wma", "WMA"),
    ("amr", "AMR (Adaptive Multi-Rate)"),
    ("opus", "Opus (Modern Lossy)"),
    ("dsf", "DSF (DFFD)"),

    # Image
    ("jpg", "JPG (JPEG)"),
    ("png", "PNG (Lossless)"),
    ("gif", "GIF (Animated)"),
    ("tiff", "TIFF (Lossless, High Quality)"),
    ("bmp", "BMP (Uncompressed)"),
    ("psd", "PSD (Photoshop Document)"),
    ("heic", "HEIC (High Efficiency Image Coding)"),
    ("svg", "SVG (Scalable Vector Graphics)"),
    ("webp", "WebP (Modern, Lossy)"),
    ("raw", "RAW (Camera Sensor Data)"),

    # Text
    ("txt", "Plain Text"),
    ("doc", "Microsoft Word Document"),
    ("docx", "Microsoft Word Document (Modern)"),
    ("pdf", "PDF (Portable Document Format)"),
    ("odt", "OpenDocument Text"),
    ("rtf", "Rich Text Format"),
    ("html", "HTML (Web Page)"),
    ("csv", "CSV (Comma-Separated Values)"),
    ("tsv", "TSV (Tab-Separated Values)"),
    ("xlsx", "XSLX(Microsoft Excel Spreadsheet)"),
    ("json", "JSON (JavaScript Object Notation)"),

    # # Video
    # ("mp4", "MP4 (H.264)"),
    # ("mov", "MOV (QuickTime)"),
    # ("avi", "AVI (Various Codecs)"),
    # ("mkv", "MKV (Matroska)"),
    # ("webm", "WebM (VP8/VP9)"),
    # ("wmv", "WMV (Windows Media Video)"),
    # ("flv", "FLV (Flash Video)"),
    # ("mpeg", "MPEG (Various Standards)"),
    # ("avchd", "AVCHD (High Definition)"),
    # ("3gp", "3GP (Mobile Devices)"),
)


SOURCE_CHOICES = (
    ("Primary", "Primary"), 
    ("Secondary", "Secondary"), 
)

FORM_CHOICES = (
    ("Raw", "Raw Data"),
    ("Processed", "Processed Data / Clean Data"),
)


class YearInput(DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs['format'] = '%Y'
        super().__init__(**kwargs)

class DatasetForm(forms.ModelForm):
    data_type = forms.ChoiceField(
        required=False,
        widget=Select2Widget,
        choices=DATA_TYPE_CHOICES
    )
    file_format = forms.ChoiceField(
        required=False,
        widget=Select2Widget,
        choices=FILE_FORMAT_CHOICES
    )
    source = forms.ChoiceField(
        required=False,
        widget=Select2Widget,
        choices=SOURCE_CHOICES
    )
    form = forms.ChoiceField(
        required=False,
        widget=Select2Widget,
        choices=FORM_CHOICES
    )

    category = forms.MultipleChoiceField(
        required=False,
        widget=Select2MultipleWidget,
        choices=CATEGORY_CHOICES
    )

    class Meta:
        model = Dataset
        exclude = ["overview"]
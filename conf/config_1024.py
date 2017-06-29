# coding=utf-8
# ����Ϊһ��*�հ�*�����ļ�, ������Ϊ�Լ�������������Ļ���
# ���а�����һЩ����ľ�̬��Դվ, ���Լ��ٿ����Ѷ�
# ��������, ����zmirror�Ļ���, �������������.com��.net��������Ӱ������. ���������׺������Ҳֻ�е�һ����Ӱ������
#
# ��������ѡ�����ϸ�����뿴 config_default.py �ж�Ӧ�Ĳ���
# �������ļ��ٶ���ķ�����������ǽ��
# ���������������ǽ��(�����ڱ��ػ����²���, ���޸�`Proxy Settings`�е�����
#
# boilerplate version: 1.0.0

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = '127.0.0.1'  # !!!����������!!!! �����޸�!
my_host_scheme = 'https://'  # ������Э��, ��ѡΪ "http://" �� "https://"
verbose_level = 2
# ############## Target Domain Settings ##############
target_domain = 'www.t66y.com'  # !!!!���Ŀ������!!!!
target_scheme = 'https://'

# ������󲿷���������ͨ�� `enable_automatic_domains_whitelist` �Զ��ɼ���, ��ֻ�ǰ����Ǹ��������������
# ʵ�ʾ���һ���µ�վʱ, �ֶ�ֻ��Ҫ��Ӻ��ٵļ��������Ϳ�����.
# �Զ��ɼ�(��������Ļ�)�᲻�ϸ�����������
external_domains = [
    #"www.t66y.com",
    "www.viidii.info",
]

# ��Щ��һЩ�����ľ�̬��Դ����, �ᱻ�Զ���ӵ�������� external_domains ��
BOILERPLATE_EXTERNAL_DOMAINS = [

    # Google����
    'www.google.com',
    'ssl.gstatic.com',
    'accounts.google.com',
    'apis.google.com',
    'www.gstatic.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'csi.gstatic.com',
    'www.googleapis.com',
    'fonts.googleapis.com',
    'ajax.googleapis.com',
    'manifest.googlevideo.com',
    'storage.googleapis.com',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    's-v6exp1-ds.metric.gstatic.com',
    'ci4.googleusercontent.com',
    'gp3.googleusercontent.com',
    'accounts.gstatic.com',
    # For Google Map (optional)
    'maps-api-ssl.google.com',
    'maps.gstatic.com',
    'maps.google.com',
    'fonts.gstatic.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',
    '-v6exp3-v4.metric.gstatic.com',
    '-v6exp3-ds.metric.gstatic.com',
    'if-v6exp3-v4.metric.gstatic.com',
    'maps.googleapis.com',
    'myphonenumbers-pa.googleapis.com',
    'plus.googleapis.com',
    'youtube.googleapis.com',
    "www-onepick-opensocial.googleusercontent.com",

    # youtube, ���ܲ��ܿ���Ƶ, ����һЩ��̬��Դ����м���
    "www.youtube.com",
    'accounts.youtube.com',
    "s.ytimg.com",
    'i.ytimg.com',
    'i1.ytimg.com',
    'yt3.ggpht.com',

    # facebook, ͬyoutube
    "facebook.com",
    "ssl.facebook.com",
    "staticxx.facebook.com",
    "api.facebook.com",
    "secure.facebook.com",
    "zh-cn.facebook.com",

    # twitter��̬����
    'g2.twimg.com',
    'hca.twimg.com',
    'g.twimg.com',
    'video.twimg.com',
    'ma.twimg.com',
    'abs.twimg.com',
    'pbs.twimg.com',
    'ton.twimg.com',
    'ma-0.twimg.com',
    'ma-1.twimg.com',
    'ma-2.twimg.com',
    'o.twimg.com',
    'abs-0.twimg.com',
    'abs-1.twimg.com',
    'abs-2.twimg.com',
    'amp.twimg.com',

    # cdnjs
    "cdnjs.cloudflare.com",
    # ΢������cdn
    "ajax.aspnetcdn.com",
    # js deliver cdn
    "cdn.jsdelivr.net",
    # jquery cdn
    "code.jquery.com",
    # boostrap-maxcdn
    "maxcdn.bootstrapcdn.com",
]

# ���������վ��ᱻǿ��ʹ��HTTPS, �ݲ�֧��ͨ���
force_https_domains = [
    # "example.com",
    # "example.org",
]

# �Զ���̬�������
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    # ���������ͨ�����д����, ������������:
    "*.cnzz.com",
    "*.viidii.info",
    # "*.*.*",
)

# ############## Proxy Settings ##############
# �������ǽ��ʹ�ñ������ļ�, ��ָ��һ��ǽ���http����
is_use_proxy = False
# ����ĸ�ʽ��SOCKS����, �뿴 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ### �����߼������뿴 config_default.py �е���ϸ˵��


# ------------ ���²���ΪһЩ�򵥵��߼�, �벻Ҫ�޸�����Ĵ��� ----------------
external_domains += BOILERPLATE_EXTERNAL_DOMAINS  # ��������̬��Դ�������뵽external_domains��
# ��������̬��Դ��������Ϊǿ��HTTPS
if force_https_domains == "NONE":
    force_https_domains = BOILERPLATE_EXTERNAL_DOMAINS
elif isinstance(force_https_domains, (list, tuple)):
    force_https_domains = list(force_https_domains) + BOILERPLATE_EXTERNAL_DOMAINS
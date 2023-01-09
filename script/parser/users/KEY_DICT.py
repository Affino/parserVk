
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
DOMAIN = 'domain'
ONLINE = 'online'
LAST_SEEN = 'last_seen'
GENDER = 'sex'
PHOTO = 'photo_max'
FOLLOWERS = 'followers_count'
B_DATE = 'bdate'
CITY = 'city'
COUNTRY = 'country'
MOBILE_PHONE = 'mobile_phone'
RELATION = 'relation'
STATUS = 'status'

ACTIVITIES = 'activities'
INTERESTS = 'interests'
MUSIC = 'music'
MOVIES = 'movies'
TV = 'tv'
BOOKS = 'books'
GAMES = 'games'
QUOTES = 'quotes'
ABOUT = 'about'

UNIVERSITY_NAME = 'university_name'
FACULTY_NAME = 'faculty_name'
EDUCATION_STATUS = 'education_status'
GRADUATION = 'graduation'

SCHOOLS = 'schools'

# COUNTERS = 'counters'
# MILITARY = 'military'
CAREER = 'career'
RELATIVES = 'relatives'
PERSONAL = 'personal'

FIRST_KEYS: list[str] = [
    DOMAIN,
    FIRST_NAME,
    LAST_NAME,
    ONLINE,
    LAST_SEEN,  # dict √
    GENDER,
    PHOTO,
    FOLLOWERS,
    B_DATE,
    CITY,       # dict √
    COUNTRY,    # dict √
    MOBILE_PHONE,
    RELATION,
    STATUS,

    ACTIVITIES,
    INTERESTS,
    MUSIC,
    MOVIES,
    TV,
    BOOKS,
    GAMES,
    QUOTES,
    ABOUT,

    UNIVERSITY_NAME,
    FACULTY_NAME,
    EDUCATION_STATUS,
    GRADUATION,

    SCHOOLS,
    # COUNTERS,
    # MILITARY,
    CAREER,
    RELATIVES,
    PERSONAL
]


schools = [
            'name',
            'year_from',
            'year_graduated',
            'year_to',
            'speciality',
        ]

military = [
            'unit',
            'from',
            'until',
        ]
counters = [
            'albums', 'audios', 'followers',
            'friends', 'gifts', 'groups',
            'online_friends', 'pages', 'photos',
            'subscriptions', 'videos', 'mutual_friends',
            'clips_followers', 'user_photos',

        ]

personals = [
            'political',
            'alcohol',
            'religion',
            'smoking',
            'life_main',
            'people_main',
            'inspired_by',
        ]

careers = [
            'company',
            'from',
            'until',
            'position',
        ]


relatives = [
            'parent',
            'sibling',
            'child',
            'grandparent',
            'grandchild',

        ]




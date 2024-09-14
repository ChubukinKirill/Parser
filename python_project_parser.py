import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
 
 
cookies = {
    'yashr': '1736459751713710347',
    'gdpr': '0',
    '_ym_uid': '1668964241371024028',
    'yuidss': '6973905991693411049',
    'location': '1',
    'crookie': 'eqRZwvuT7mXgqoTS5jN7kRFpsQL9qpRWZXTnKAQ4b730kZpSWIIDcsr54IolcNkyu4oaK/oay4O+hCFU5u6MHETD4b4=',
    'cmtchd': 'MTcxMzcxMDM0ODU3NA==',
    'coockoos': '4',
    'i': 'UDJ3z7AsUqHDLVRGrVaXrpcF0+zP+xXZEBFZ/PzIDZSEnxLndNp7lNqtCGThbW6kP0oqiOazu2GIImTcY99aW6pkyyI=',
    'yandexuid': '6973905991693411049',
    'PHPSESSID': 'dd91479d4a7fcc6f0f2848c7a04a09b3',
    'yandex_gid': '21623',
    'mobile': 'no',
    'mda_exp_enabled': '1',
    'my_perpages': '%5B%5D',
    'sso_status': 'sso.passport.yandex.ru:synchronized',
    'no-re-reg-required': '1',
    '_ym_isad': '1',
    'yp': '1714044409.yu.6973905991693411049',
    'ymex': '1716550009.oyu.6973905991693411049',
    'tc': '6101',
    'uid': '16987894',
    '_yasc': 'd/Ti2QCveYdvvYp0DRSFCStAzF0McixErJzBrrsZVl7fO9BTAas/OuvvnTty3Rlx',
    'ya_sess_id': '3:1713962549.5.0.1663166743231:KzgnLg:34.1.2:1|466957580.-1.2|1130000061277634.-1.0.2:10891593|437380527.42697207.2.2:42697207.3:1705863950|30:10224381.899482.pB7FwceXD9N8WOQf-Cn_1NAc2v0',
    'sessar': '1.1189.CiDIc6BGHBmQ-uPlXQdMMQjbKQkFvanOBq3LPtADiTJQCw.pyukw4YnMBX20tK47s2yHeOKQ0h7FQUbBA9HPbRm6hA',
    'yandex_login': 'kikoman89rus',
    'ys': 'udn.cDrQmtC40YDQuNC70Lsg0KfRg9Cx0YPQutC40L0%3D#c_chck.561950728',
    'L': 'd19bCXwHYGl+UXFXBF5mVm8Ed1ZAR29oJBgDOzQIX1wKCg07.1713962549.15694.346881.dd5f62869bbcaa55c42475d12abf62c1',
    'mda2_beacon': '1713962549591',
    '_ym_d': '1713962649',
}

headers = {
    'authority': 'graphql.kinopoisk.ru',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'yashr=1736459751713710347; gdpr=0; _ym_uid=1668964241371024028; yuidss=6973905991693411049; location=1; crookie=eqRZwvuT7mXgqoTS5jN7kRFpsQL9qpRWZXTnKAQ4b730kZpSWIIDcsr54IolcNkyu4oaK/oay4O+hCFU5u6MHETD4b4=; cmtchd=MTcxMzcxMDM0ODU3NA==; coockoos=4; i=UDJ3z7AsUqHDLVRGrVaXrpcF0+zP+xXZEBFZ/PzIDZSEnxLndNp7lNqtCGThbW6kP0oqiOazu2GIImTcY99aW6pkyyI=; yandexuid=6973905991693411049; PHPSESSID=dd91479d4a7fcc6f0f2848c7a04a09b3; yandex_gid=21623; mobile=no; mda_exp_enabled=1; my_perpages=%5B%5D; sso_status=sso.passport.yandex.ru:synchronized; no-re-reg-required=1; _ym_isad=1; yp=1714044409.yu.6973905991693411049; ymex=1716550009.oyu.6973905991693411049; tc=6101; uid=16987894; _yasc=d/Ti2QCveYdvvYp0DRSFCStAzF0McixErJzBrrsZVl7fO9BTAas/OuvvnTty3Rlx; ya_sess_id=3:1713962549.5.0.1663166743231:KzgnLg:34.1.2:1|466957580.-1.2|1130000061277634.-1.0.2:10891593|437380527.42697207.2.2:42697207.3:1705863950|30:10224381.899482.pB7FwceXD9N8WOQf-Cn_1NAc2v0; sessar=1.1189.CiDIc6BGHBmQ-uPlXQdMMQjbKQkFvanOBq3LPtADiTJQCw.pyukw4YnMBX20tK47s2yHeOKQ0h7FQUbBA9HPbRm6hA; yandex_login=kikoman89rus; ys=udn.cDrQmtC40YDQuNC70Lsg0KfRg9Cx0YPQutC40L0%3D#c_chck.561950728; L=d19bCXwHYGl+UXFXBF5mVm8Ed1ZAR29oJBgDOzQIX1wKCg07.1713962549.15694.346881.dd5f62869bbcaa55c42475d12abf62c1; mda2_beacon=1713962549591; _ym_d=1713962649',
    'origin': 'https://www.kinopoisk.ru',
    'referer': 'https://www.kinopoisk.ru/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'service-id': '25',
    'uber-trace-id': '16f49f76e0359b13:4969b026230711a0:0:1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.186 Safari/537.36',
    'x-preferred-language': 'ru',
    'x-request-id': '1713962645990662-11699074836613839476:6',
}
 
 
 
 
params = {
    'operationName': 'MovieDesktopListPage',
}
 
 
movie_urls = []
 
for offset in range(0, 250, 50):
 
    json_data = {
        'operationName': 'MovieDesktopListPage',
        'variables': {
            'slug': 'top250',
            'platform': 'DESKTOP',
            'regionId': 1,
            'withUserData': True,
            'supportedFilterTypes': [
                'BOOLEAN',
                'SINGLE_SELECT',
            ],
            'filters': {
                'booleanFilterValues': [],
                'intRangeFilterValues': [],
                'singleSelectFilterValues': [],
                'multiSelectFilterValues': [],
                'realRangeFilterValues': [],
            },
            'singleSelectFiltersLimit': 250,
            'singleSelectFiltersOffset': 0,
            'moviesLimit': 50,
            # Здесь offset вставляем, для пагинации
            'moviesOffset': offset,
            'moviesOrder': 'POSITION_ASC',
            'supportedItemTypes': [
                'COMING_SOON_MOVIE_LIST_ITEM',
                'MOVIE_LIST_ITEM',
                'TOP_MOVIE_LIST_ITEM',
                'POPULAR_MOVIE_LIST_ITEM',
                'MOST_PROFITABLE_MOVIE_LIST_ITEM',
                'MOST_EXPENSIVE_MOVIE_LIST_ITEM',
                'BOX_OFFICE_MOVIE_LIST_ITEM',
                'OFFLINE_AUDIENCE_MOVIE_LIST_ITEM',
                'RECOMMENDATION_MOVIE_LIST_ITEM',
            ],
        },
        'query': 'query MovieDesktopListPage($slug: String!, $platform: WebClientPlatform!, $withUserData: Boolean!, $regionId: Int!, $supportedFilterTypes: [FilterType]!, $filters: FilterValuesInput, $singleSelectFiltersLimit: Int!, $singleSelectFiltersOffset: Int!, $moviesLimit: Int, $moviesOffset: Int, $moviesOrder: MovieListItemOrderBy, $supportedItemTypes: [MovieListItemType]) { movieListBySlug(slug: $slug, supportedFilterTypes: $supportedFilterTypes, filters: $filters) { id name description cover { avatarsUrl __typename } ...MovieListCompositeName ...MovieListAvailableFilters ...MovieList ...DescriptionLink __typename } webPage(platform: $platform) { kpMovieListPage(movieListSlug: $slug) { htmlMeta { ...OgImage __typename } footer { ...FooterConfigData __typename } featuring { ...MovieListFeaturingData __typename } __typename } __typename } } fragment ToggleFilter on BooleanFilter { id enabled name { russian __typename } __typename } fragment SingleSelectFilters on SingleSelectFilter { id name { russian __typename } hint { russian __typename } values(offset: $singleSelectFiltersOffset, limit: $singleSelectFiltersLimit) { items { name { russian __typename } selectable value __typename } __typename } __typename } fragment MovieListUserData on Movie { userData { folders { id name public __typename } watchStatuses { notInterested { value __typename } watched { value __typename } __typename } voting { value votedAt __typename } __typename } __typename } fragment MovieListCompositeName on MovieListMeta { compositeName { parts { ... on FilterReferencedMovieListNamePart { filterValue { ... on SingleSelectFilterValue { filterId __typename } __typename } name __typename } ... on StaticMovieListNamePart { name __typename } __typename } __typename } __typename } fragment MovieListAvailableFilters on MovieListMeta { availableFilters { items { ... on BooleanFilter { ...ToggleFilter __typename } ... on SingleSelectFilter { ...SingleSelectFilters __typename } __typename } __typename } __typename } fragment MovieList on MovieListMeta { movies(limit: $moviesLimit, offset: $moviesOffset, orderBy: $moviesOrder, supportedItemTypes: $supportedItemTypes) { total items { movie { id contentId title { russian original __typename } poster { avatarsUrl fallbackUrl __typename } countries { id name __typename } genres { id name __typename } cast: members(role: [ACTOR], limit: 3) { items { details person { name originalName __typename } __typename } __typename } directors: members(role: [DIRECTOR], limit: 1) { items { details person { name originalName __typename } __typename } __typename } url rating { kinopoisk { isActive count value __typename } expectation { isActive count value __typename } __typename } mainTrailer { id isEmbedded __typename } viewOption { buttonText originalButtonText promotionIcons { avatarsUrl fallbackUrl __typename } isAvailableOnline: isWatchable(filter: {anyDevice: false, anyRegion: false}) purchasabilityStatus type rightholderLogoUrlForPoster availabilityAnnounce { availabilityDate type groupPeriodType announcePromise __typename } __typename } isTicketsAvailable(regionId: $regionId) ... on Film { productionYear duration isShortFilm top250 __typename } ... on TvSeries { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on MiniSeries { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on TvShow { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on Video { productionYear duration isShortFilm __typename } ...MovieListUserData @include(if: $withUserData) __typename } ... on TopMovieListItem { position positionDiff rate votes __typename } ... on MostProfitableMovieListItem { boxOffice { amount __typename } budget { amount __typename } ratio __typename } ... on MostExpensiveMovieListItem { budget { amount __typename } __typename } ... on OfflineAudienceMovieListItem { viewers __typename } ... on PopularMovieListItem { positionDiff __typename } ... on BoxOfficeMovieListItem { boxOffice { amount __typename } __typename } ... on RecommendationMovieListItem { __typename } ... on ComingSoonMovieListItem { releaseDate { date accuracy __typename } __typename } __typename } __typename } __typename } fragment DescriptionLink on MovieListMeta { descriptionLink { title url __typename } __typename } fragment OgImage on HtmlMeta { openGraph { image { avatarsUrl __typename } __typename } __typename } fragment FooterConfigData on FooterConfiguration { socialNetworkLinks { icon { avatarsUrl __typename } url title __typename } appMarketLinks { icon { avatarsUrl __typename } url title __typename } links { title url __typename } __typename } fragment MovieListFeaturingData on MovieListFeaturing { items { title url __typename } __typename } ',
    }
 
    r = requests.post('https://graphql.kinopoisk.ru/graphql/', cookies=cookies, params=params, headers=headers, json=json_data)
    json_data: dict = r.json()['data']['movieListBySlug']['movies']['items']
 
    for item in json_data:
        movie_url = item['movie']['url']
        movie_urls.append(movie_url)
 
 
def find_next_div(s):
 
    """Функция принимает строку для поиска атрибута div в котором text равен данной строке
    и возвращает этот div либо None."""
 
    if soup.find('div', string=s) is not None:
        return soup.find('div', string=s).find_next('div')
    return None
 
 
# список для сбора данных о фильмах
movies = []
 
for movie_url in movie_urls:
    r = requests.get(movie_url, cookies=cookies, headers=headers)
    soup = bs(r.text, 'lxml')
    # название
    name = soup.h1.text.split(' (')[0]
    # рейтинг топ-250
    top_250 = int(soup.find('span', {'class': 'styles_position__pm10U'}).text.split(' место')[0])
    # рейтинг
    rating = soup.find('span', {'class': 'styles_ratingKpTop__84afd'}).text.replace('.', ',')
 
    # год
    year = find_next_div('Год производства').text if find_next_div('Год производства') is not None else '?'
    # страна
    country = find_next_div('Страна').text if find_next_div('Страна') is not None else '?'
    # жанр
    genre = find_next_div('Жанр').text.split(', ')[0] if find_next_div('Жанр') is not None else '?'
    # Режиссер
    director = find_next_div('Режиссер').text.split(', ')[0] if find_next_div('Режиссер') is not None else '?'
    # Сценарист
    scenario = find_next_div('Сценарий').text.split(', ')[0] if find_next_div('Сценарий') is not None else '?'
    # Продюсер
    producer = find_next_div('Продюсер').text.split(', ')[0] if find_next_div('Продюсер') is not None else '?'
 
    if find_next_div('Бюджет') is not None:
        if find_next_div('Бюджет').text[0] == '€' or find_next_div('Бюджет').text[0] == '$':
            # бюджет
            budget = int(find_next_div('Бюджет').text[1:].replace('\xa0', ''))
            # валюта
            currency = find_next_div('Бюджет').text[0]
        else:
            # бюджет
            budget = int(find_next_div('Бюджет').text.split(' ', maxsplit=1)[1].replace('\xa0', ''))
            # валюта
            currency = find_next_div('Бюджет').text.split(' ', maxsplit=1)[0]
    else:
        budget = '?'
        currency = '?'
 
    # Сборы в США
    income_usa = int(find_next_div('Сборы в США').text.replace('$', '').replace('сборы', '').replace('€', '').replace('\xa0', '')) \
        if find_next_div('Сборы в США') is not None else '?'
    # Сборы в мире
    income_world = int(find_next_div('Сборы в мире').text.split('=')[-1].replace('сборы', '').replace('$', '')
                       .replace('€', '').replace('\xa0', '')) if find_next_div('Сборы в мире') is not None else '?'
    # Сборы в России
    income_russia = int(find_next_div('Сборы в России').text.replace('сборы', '').replace('$', '').replace('€', '').replace('\xa0', '')) \
        if find_next_div('Сборы в России') is not None else '?'
 
    # возраст
    age = find_next_div('Возраст').text if find_next_div('Возраст') is not None else '?'
    # рейтинг MPAA
    rating_mpaa = find_next_div('Рейтинг MPAA').span.text if find_next_div('Рейтинг MPAA') is not None else '?'
    # время
    duration = int(find_next_div('Время').text.split(' мин')[0]) if find_next_div('Время') is not None else '?'
 
    movies.append({
        'Название': name,
        'ТОП-250': top_250,
        'Рейтинг': rating,
        'Страна': country,
        'Жанр': genre,
        'Режиссер': director,
        'Сценарист': scenario,
        'Продюссер': producer,
        'Бюджет': budget,
        'Валюта бюджета': currency,
        'Сборы в США': income_usa,
        'Сборы в мире': income_world,
        'Сборы в России': income_russia,
        'Возраст': age,
        'Рейтинг MPAA': rating_mpaa,
        'Время': duration
    })
    print(name)
 
df = pd.DataFrame(movies)
df.to_csv('топ-250.csv', sep=';', encoding='utf-8-sig', index=False)
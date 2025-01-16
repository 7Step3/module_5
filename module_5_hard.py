import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        return self.password == other.password

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {user.nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        # print(f"Пользователь {nickname} зарегистрирован.")

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                # print(f"Пользователь {nickname} вошёл в аккаунт.")
                return
        print('Неверный логин или пароль')

    def add(self, title: str, duration: int, adult_mode: bool = False):
        new_video = Video(title, duration)
        self.videos.append(new_video)
        # print(f"Видео '{title}' добавлено.")

    def get_video(self, search_word: str):
        search_word = search_word.lower()
        results = []
        for video in self.videos:
            if search_word in video.title.lower():
                results.append(video)
        if results:
            return results

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_found = False
        for video in self.videos:
            if video.title == title:
                video_found = True
                if self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(1, video.duration + 1):
                    print(second)
                    time.sleep(1)
                print("Конец видео")
                return


ur = UrTube()
# Добавление видео
ur.add('Лучший язык программирования 2024 года', 200)
ur.add('Для чего девушкам парень программист?', 10, adult_mode=True)
# Проверка поиска
print(ur.get_video('лучший'))
print(ur.get_video('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

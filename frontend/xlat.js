function xlat() {
  dict = {
    "Enemy spotted": {
      "sv": "Fiende siktad",
      "ru": "Враг замечен",
      "uk": "Ворог помічений"
    },
    "Place your marker as accurately as possible!": {
      "sv": "Placera din markör så noga du kan!",
      "ru": "Разместите маркер как можно точнее!",
      "uk": "Розмістіть свій маркер якомога точніше!"
    },
    "Unit type": {
      "sv": "Enhetstyp",
      "ru": "Тип устройства",
      "uk": "Тип агрегату"
    },
    "Infantry": {
      "sv": "Infanteri",
      "ru": "Пехота",
      "uk": "Піхота"
    },
    "Guerilla": {
      "sv": "Gerilla",
      "ru": "Партизан",
      "uk": "Партизанська"
    },
    "Paratrooper": {
      "sv": "Fallskärmsjägare",
      "ru": "Десантник",
      "uk": "Десантник"
    },
    "Artillery": {
      "sv": "Artilleri",
      "ru": "Артиллерия",
      "uk": "Артилерія"
    },
    "Tank": {
      "sv": "Stridsvagn",
      "ru": "Танк",
      "uk": "Танк"
    },
    "Combat vehicle": {
      "sv": "Stridsfordon",
      "ru": "",
      "uk": "Бойова машина"
    },
    "Vehicle": {
      "sv": "Fordon",
      "ru": "Средство передвижения",
      "uk": "Фордон"
    },
    "Other": {
      "sv": "Annat",
      "ru": "Другой",
      "uk": "Інший"
    },
    "Number of units": {
      "sv": "Antal enheter",
      "ru": "Количество единиц",
      "uk": "Кількість одиниць"
    },
    "Minutes ago": {
      "sv": "Minuter sedan",
      "ru": "Минут назад",
      "uk": "Хвилин тому"
    },
    "Heading, speed, activity, notes": {
      "sv": "Riktning, fart, aktivitet, noteringar",
      "ru": "Заголовок, скорость, активность, заметки",
      "uk": "Заголовок, швидкість, активність, нотатки"
    },
    "Submit": {
      "sv": "Skicka",
      "ru": "Подавать",
      "uk": "Надіслати"
    },
    "You need to zoom in further to place troops!": {
      "sv": "Du måste zooma in mer för att placera trupper!",
      "ru": "Вам нужно увеличить масштаб, чтобы разместить войска!",
      "uk": "Вам потрібно збільшити ще більше, щоб розмістити війська!"
    },
    "How many did you see?": {
      "sv": "Hur många såg du?",
      "ru": "Сколько ты видел?",
      "uk": "Скільки ви бачили?"
    },
    "How long time ago was this?": {
      "sv": "Hur länge sedan var detta?",
      "ru": "Как давно это было?",
      "uk": "Як давно це було?"
    }
  };
  $(".xlat").each(function() {
    let text = $(this).text();
    let key = text || $(this).val();
    let o = dict[key];
    let lang = (navigator.language || navigator.userLanguage).replace(/-.*/, '');
    let s = o && o[lang] || key;
    text ? $(this).text(s) : $(this).val(s);
  });
}

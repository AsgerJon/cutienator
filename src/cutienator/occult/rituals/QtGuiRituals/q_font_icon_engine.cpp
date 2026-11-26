//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfonticonengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfonticonengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFontIconEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFontIconEngine : QFontIconEngine {
  using QFontIconEngine::string;
  using QFontIconEngine::glyph;
};

//  A QFontIconEngine that Python can take functions over in. Every QFontIconEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQFontIconEngineCall0)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef bool (*CuteQFontIconEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQFontIconEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void * (*CuteQFontIconEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QSize * (*CuteQFontIconEngineCall4)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQFontIconEngineCall5)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQFontIconEngineCall6)(const void *, const QSize *, int, int, qreal, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQFontIconEngineCall7)(const void *, QPainter *, const QRect *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQFontIconEngineCall8)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef glyph_t (*CuteQFontIconEngineCall9)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
typedef void (*CuteQFontIconEngineCall10)(const void *, const QPixmap *, int, int, int *);
typedef void (*CuteQFontIconEngineCall11)(const void *, const QString *, const QSize *, int, int, int *);
typedef void (*CuteQFontIconEngineCall12)(const void *, int, void *, int *);
class CuteQFontIconEngine : public QFontIconEngine {
public:
  using QFontIconEngine::QFontIconEngine;
  CuteQFontIconEngine(const QFontIconEngine & other) : QFontIconEngine(other) {}
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine8iconNameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine3keyEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine5cloneEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK15QFontIconEngine6stringEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK15QFontIconEngine5glyphEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine12virtual_hookEiPv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_ICON)
  //  QString QFontIconEngine::iconName()
  QString iconName() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontIconEngineCall0 call = reinterpret_cast<CuteQFontIconEngineCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontIconEngine::iconName();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  bool QFontIconEngine::isNull()
  bool isNull() override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontIconEngineCall1 call = reinterpret_cast<CuteQFontIconEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontIconEngine::isNull();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QFontIconEngine::key() const
  QString key() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontIconEngineCall2 call = reinterpret_cast<CuteQFontIconEngineCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontIconEngine::key();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QIconEngine *QFontIconEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontIconEngineCall3 call = reinterpret_cast<CuteQFontIconEngineCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QFontIconEngine::clone();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QSize QFontIconEngine::actualSize(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QSize actualSize(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontIconEngineCall4 call = reinterpret_cast<CuteQFontIconEngineCall4>(taken[4]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QFontIconEngine::actualSize(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QFontIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontIconEngineCall5 call = reinterpret_cast<CuteQFontIconEngineCall5>(taken[5]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QFontIconEngine::pixmap(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QFontIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontIconEngineCall6 call = reinterpret_cast<CuteQFontIconEngineCall6>(taken[6]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QFontIconEngine::scaledPixmap(size, mode, state, scale);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QFontIconEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(
      QPainter *painter,
      const QRect &rect,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontIconEngineCall7 call = reinterpret_cast<CuteQFontIconEngineCall7>(taken[7]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QFontIconEngine::paint(painter, rect, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QFontIconEngine::string() const
  QString string() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontIconEngineCall8 call = reinterpret_cast<CuteQFontIconEngineCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontIconEngine::string();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  glyph_t QFontIconEngine::glyph() const
  glyph_t glyph() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontIconEngineCall9 call = reinterpret_cast<CuteQFontIconEngineCall9>(taken[9]);
      glyph_t given = call(this, &handled);
      if (handled) return given;
    }
    return QFontIconEngine::glyph();
  }
#endif  // !defined(QT_NO_ICON)

  //  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
  //      QIcon::State state)
  void addPixmap(
      const QPixmap &pixmap,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontIconEngineCall10 call = reinterpret_cast<CuteQFontIconEngineCall10>(taken[10]);
      call(this, &pixmap, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addPixmap(pixmap, mode, state);
  }

  //  void QIconEngine::addFile(const QString &fileName, const QSize &size,
  //      QIcon::Mode mode, QIcon::State state)
  void addFile(
      const QString &fileName,
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontIconEngineCall11 call = reinterpret_cast<CuteQFontIconEngineCall11>(taken[11]);
      call(this, &fileName, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addFile(fileName, size, mode, state);
  }

  //  void QIconEngine::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontIconEngineCall12 call = reinterpret_cast<CuteQFontIconEngineCall12>(taken[12]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QIconEngine::virtual_hook(id, data);
  }
};

//  QFontIconEngine::QFontIconEngine(const QString &iconName, const QFont
//      &font)
extern "C" Q_DECL_EXPORT
QFontIconEngine *ritual_ZN15QFontIconEngineC1ERK7QStringRK5QFont(
    const QString *iconName,
    const QFont *font) {
  return new CuteQFontIconEngine(*iconName, *font);
}

//  QFontIconEngine::~QFontIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QFontIconEngineD1Ev(QFontIconEngine *self) {
  delete self;
}

//  QString QFontIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QFontIconEngine8iconNameEv(QFontIconEngine *self) {
  return new QString(self->iconName());
}

//  bool QFontIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QFontIconEngine6isNullEv(QFontIconEngine *self) {
  return self->isNull();
}

//  QString QFontIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QFontIconEngine3keyEv(const QFontIconEngine *self) {
  return new QString(self->key());
}

//  QIconEngine *QFontIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK15QFontIconEngine5cloneEv(
    const QFontIconEngine *self) {
  return self->clone();
}

//  QList<QSize> QFontIconEngine::availableSizes(QIcon::Mode a0, QIcon::State
//      a1)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN15QFontIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QFontIconEngine *self,
    QIcon::Mode a0,
    QIcon::State a1) {
  return new QList<QSize>(self->availableSizes(a0, a1));
}

//  QSize QFontIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN15QFontIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QPixmap QFontIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN15QFontIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  QPixmap QFontIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN15QFontIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  void QFontIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QFontIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QFontIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QString QFontIconEngine::string() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QFontIconEngine6stringEv(const QFontIconEngine *self) {
  return new QString(self->string());
}

//  glyph_t QFontIconEngine::glyph() const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK15QFontIconEngine5glyphEv(const QFontIconEngine *self) {
  return self->glyph();
}

//  quint64 QFontIconEngine::calculateCacheKey(QIcon::Mode mode, QIcon::State
//      state)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QFontIconEngine17calculateCacheKeyEN5QIcon4ModeENS0_5StateE(
    QIcon::Mode mode,
    QIcon::State state) {
  return QFontIconEngine::calculateCacheKey(mode, state);
}

//  a Python function taken by a CuteQFontIconEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontIconEngine(
    QFontIconEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontIconEngine *>(self)->take(key, call);
}

//  QString QFontIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN15QFontIconEngine8iconNameEv(QFontIconEngine *self) {
  return new QString(self->QFontIconEngine::iconName());
}

//  bool QFontIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QFontIconEngine6isNullEv(QFontIconEngine *self) {
  return self->QFontIconEngine::isNull();
}

//  QString QFontIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QFontIconEngine3keyEv(const QFontIconEngine *self) {
  return new QString(self->QFontIconEngine::key());
}

//  QIconEngine *QFontIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK15QFontIconEngine5cloneEv(
    const QFontIconEngine *self) {
  return self->QFontIconEngine::clone();
}

//  QSize QFontIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN15QFontIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QFontIconEngine::actualSize(*size, mode, state));
}

//  QPixmap QFontIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN15QFontIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QFontIconEngine::pixmap(*size, mode, state));
}

//  QPixmap QFontIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN15QFontIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QFontIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(
      self->QFontIconEngine::scaledPixmap(
          *size,
          mode,
          state,
          scale));
}

//  void QFontIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QFontIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QFontIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QFontIconEngine::paint(painter, *rect, mode, state);
}

//  QString QFontIconEngine::string() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QFontIconEngine6stringEv(
    const QFontIconEngine *self) {
  return new QString(
      static_cast<const OwnQFontIconEngine *>(self)->OwnQFontIconEngine::string());
}

//  glyph_t QFontIconEngine::glyph() const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK15QFontIconEngine5glyphEv(
    const QFontIconEngine *self) {
  return static_cast<const OwnQFontIconEngine *>(self)->OwnQFontIconEngine::glyph();
}

#endif  // !defined(QT_NO_ICON)

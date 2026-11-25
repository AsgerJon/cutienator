//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qappleiconengine_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Not written: 'virtual_hook', which the generator leaves out of
//  QIconEngine and every class built on it.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qappleiconengine_p.h>
#include <QtGui/qicon.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qlist.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAppleIconEngine that Python can take functions over in. Every
//  QAppleIconEngine Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void * (*CuteQAppleIconEngineCall0)(const void *, int *);
typedef QString * (*CuteQAppleIconEngineCall1)(const void *, int *);
typedef QString * (*CuteQAppleIconEngineCall2)(const void *, int *);
typedef bool (*CuteQAppleIconEngineCall3)(const void *, int *);
typedef const QSize * (*CuteQAppleIconEngineCall4)(const void *, const QSize *, int, int, int *);
typedef const QPixmap * (*CuteQAppleIconEngineCall5)(const void *, const QSize *, int, int, int *);
typedef const QPixmap * (*CuteQAppleIconEngineCall6)(const void *, const QSize *, int, int, qreal, int *);
typedef void (*CuteQAppleIconEngineCall7)(const void *, QPainter *, const QRect *, int, int, int *);
typedef void (*CuteQAppleIconEngineCall8)(const void *, const QPixmap *, int, int, int *);
typedef void (*CuteQAppleIconEngineCall9)(const void *, const QString *, const QSize *, int, int, int *);
class CuteQAppleIconEngine : public QAppleIconEngine {
public:
  using QAppleIconEngine::QAppleIconEngine;
  CuteQAppleIconEngine(const QAppleIconEngine &other) : QAppleIconEngine(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QIconEngine5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QIconEngine3keyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine8iconNameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  QIconEngine *QAppleIconEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAppleIconEngineCall0 call = reinterpret_cast<CuteQAppleIconEngineCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QAppleIconEngine::clone();
  }

  //  QString QAppleIconEngine::key() const
  QString key() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAppleIconEngineCall1 call = reinterpret_cast<CuteQAppleIconEngineCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAppleIconEngine::key();
  }

  //  QString QAppleIconEngine::iconName()
  QString iconName() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAppleIconEngineCall2 call = reinterpret_cast<CuteQAppleIconEngineCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAppleIconEngine::iconName();
  }

  //  bool QAppleIconEngine::isNull()
  bool isNull() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAppleIconEngineCall3 call = reinterpret_cast<CuteQAppleIconEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAppleIconEngine::isNull();
  }

  //  QSize QAppleIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QSize actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAppleIconEngineCall4 call = reinterpret_cast<CuteQAppleIconEngineCall4>(taken[4]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QAppleIconEngine::actualSize(size, mode, state);
  }

  //  QPixmap QAppleIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAppleIconEngineCall5 call = reinterpret_cast<CuteQAppleIconEngineCall5>(taken[5]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QAppleIconEngine::pixmap(size, mode, state);
  }

  //  QPixmap QAppleIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAppleIconEngineCall6 call = reinterpret_cast<CuteQAppleIconEngineCall6>(taken[6]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QAppleIconEngine::scaledPixmap(size, mode, state, scale);
  }

  //  void QAppleIconEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAppleIconEngineCall7 call = reinterpret_cast<CuteQAppleIconEngineCall7>(taken[7]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QAppleIconEngine::paint(painter, rect, mode, state);
  }

  //  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
  //      QIcon::State state)
  void addPixmap(const QPixmap &pixmap, QIcon::Mode mode, QIcon::State state) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAppleIconEngineCall8 call = reinterpret_cast<CuteQAppleIconEngineCall8>(taken[8]);
      call(this, &pixmap, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addPixmap(pixmap, mode, state);
  }

  //  void QIconEngine::addFile(const QString &fileName, const QSize &size,
  //      QIcon::Mode mode, QIcon::State state)
  void addFile(const QString &fileName, const QSize &size, QIcon::Mode mode, QIcon::State state) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAppleIconEngineCall9 call = reinterpret_cast<CuteQAppleIconEngineCall9>(taken[9]);
      call(this, &fileName, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addFile(fileName, size, mode, state);
  }
};

//  QAppleIconEngine::QAppleIconEngine(const QString &iconName)
extern "C" Q_DECL_EXPORT
QAppleIconEngine *ritual_ZN16QAppleIconEngineC1ERK7QString(
    const QString *iconName) {
  return new CuteQAppleIconEngine(*iconName);
}

//  QAppleIconEngine::~QAppleIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAppleIconEngineD1Ev(QAppleIconEngine *self) {
  delete self;
}

//  QIcon QAppleIconEngine::fromTheme(const QString &iconName)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN16QAppleIconEngine9fromThemeERK7QString(
    const QString *iconName) {
  return new QIcon(QAppleIconEngine::fromTheme(*iconName));
}

//  QIconEngine *QAppleIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QAppleIconEngine5cloneEv(
    const QAppleIconEngine *self) {
  return self->clone();
}

//  QString QAppleIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAppleIconEngine3keyEv(const QAppleIconEngine *self) {
  return new QString(self->key());
}

//  QString QAppleIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAppleIconEngine8iconNameEv(QAppleIconEngine *self) {
  return new QString(self->iconName());
}

//  bool QAppleIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAppleIconEngine6isNullEv(QAppleIconEngine *self) {
  return self->isNull();
}

//  QList<QSize> QAppleIconEngine::availableSizes(QIcon::Mode a0,
//      QIcon::State a1)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN16QAppleIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QAppleIconEngine *self,
    QIcon::Mode a0,
    QIcon::State a1) {
  return new QList<QSize>(self->availableSizes(a0, a1));
}

//  QSize QAppleIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN16QAppleIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QPixmap QAppleIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN16QAppleIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  QPixmap QAppleIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN16QAppleIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  void QAppleIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAppleIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QAppleIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QList<QSize> QAppleIconEngine::availableIconSizes(double aspectRatio)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN16QAppleIconEngine18availableIconSizesEd(
    double aspectRatio) {
  return new QList<QSize>(QAppleIconEngine::availableIconSizes(aspectRatio));
}

//  a Python function taken by a CuteQAppleIconEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAppleIconEngine(
    QAppleIconEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAppleIconEngine *>(self)->take(key, call);
}

//  QIconEngine *QAppleIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK16QAppleIconEngine5cloneEv(
    const QAppleIconEngine *self) {
  return self->QAppleIconEngine::clone();
}

//  QString QAppleIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QAppleIconEngine3keyEv(
    const QAppleIconEngine *self) {
  return new QString(self->QAppleIconEngine::key());
}

//  QString QAppleIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN16QAppleIconEngine8iconNameEv(QAppleIconEngine *self) {
  return new QString(self->QAppleIconEngine::iconName());
}

//  bool QAppleIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAppleIconEngine6isNullEv(QAppleIconEngine *self) {
  return self->QAppleIconEngine::isNull();
}

//  QSize QAppleIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN16QAppleIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QAppleIconEngine::actualSize(*size, mode, state));
}

//  QPixmap QAppleIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN16QAppleIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QAppleIconEngine::pixmap(*size, mode, state));
}

//  QPixmap QAppleIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN16QAppleIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QAppleIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->QAppleIconEngine::scaledPixmap(*size, mode, state, scale));
}

//  void QAppleIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAppleIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QAppleIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QAppleIconEngine::paint(painter, *rect, mode, state);
}

#endif  // defined(Q_OS_DARWIN)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qiconengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qiconengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QIconEngine that Python can take functions over in. Every QIconEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQIconEngineCall0)(const void *, QPainter *, const QRect *, int, int, int *);
typedef const QSize * (*CuteQIconEngineCall1)(const void *, const QSize *, int, int, int *);
typedef const QPixmap * (*CuteQIconEngineCall2)(const void *, const QSize *, int, int, int *);
typedef void (*CuteQIconEngineCall3)(const void *, const QPixmap *, int, int, int *);
typedef void * (*CuteQIconEngineCall4)(const void *, int *);
typedef bool (*CuteQIconEngineCall5)(const void *, int *);
typedef const QPixmap * (*CuteQIconEngineCall6)(const void *, const QSize *, int, int, qreal, int *);
class CuteQIconEngine : public QIconEngine {
public:
  using QIconEngine::QIconEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QIconEngine5cloneEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QIconEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(
      QPainter *painter,
      const QRect &rect,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconEngineCall0 call = reinterpret_cast<CuteQIconEngineCall0>(taken[0]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
  }

  //  QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QSize actualSize(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconEngineCall1 call = reinterpret_cast<CuteQIconEngineCall1>(taken[1]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QIconEngine::actualSize(size, mode, state);
  }

  //  QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQIconEngineCall2 call = reinterpret_cast<CuteQIconEngineCall2>(taken[2]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QIconEngine::pixmap(size, mode, state);
  }

  //  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
  //      QIcon::State state)
  void addPixmap(
      const QPixmap &pixmap,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[3]) {
      int handled = 0;
      CuteQIconEngineCall3 call = reinterpret_cast<CuteQIconEngineCall3>(taken[3]);
      call(this, &pixmap, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addPixmap(pixmap, mode, state);
  }

  //  QIconEngine *QIconEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQIconEngineCall4 call = reinterpret_cast<CuteQIconEngineCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return {};
  }

  //  bool QIconEngine::isNull()
  bool isNull() override {
    if (taken[5]) {
      int handled = 0;
      CuteQIconEngineCall5 call = reinterpret_cast<CuteQIconEngineCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIconEngine::isNull();
  }

  //  QPixmap QIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[6]) {
      int handled = 0;
      CuteQIconEngineCall6 call = reinterpret_cast<CuteQIconEngineCall6>(taken[6]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QIconEngine::scaledPixmap(size, mode, state, scale);
  }
};

//  QIconEngine::~QIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngineD1Ev(QIconEngine *self) {
  delete self;
}

//  void QIconEngine::paint(QPainter *painter, const QRect &rect, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addPixmap(*pixmap, mode, state);
}

//  void QIconEngine::addFile(const QString &fileName, const QSize &size,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addFile(*fileName, *size, mode, state);
}

//  QString QIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIconEngine3keyEv(const QIconEngine *self) {
  return new QString(self->key());
}

//  QIconEngine *QIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK11QIconEngine5cloneEv(const QIconEngine *self) {
  return self->clone();
}

//  QString QIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QIconEngine8iconNameEv(QIconEngine *self) {
  return new QString(self->iconName());
}

//  bool QIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QIconEngine6isNullEv(QIconEngine *self) {
  return self->isNull();
}

//  QPixmap QIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  a Python function taken by a CuteQIconEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconEngine(
    QIconEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconEngine *>(self)->take(key, call);
}

//  QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QIconEngine::actualSize(*size, mode, state));
}

//  QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QIconEngine::pixmap(*size, mode, state));
}

//  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QIconEngine::addPixmap(*pixmap, mode, state);
}

//  bool QIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QIconEngine6isNullEv(QIconEngine *self) {
  return self->QIconEngine::isNull();
}

//  QPixmap QIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(
      self->QIconEngine::scaledPixmap(
          *size,
          mode,
          state,
          scale));
}

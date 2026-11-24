//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qicon_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPixmapIconEngine that Python can take functions over in. Every QPixmapIconEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ICON)
typedef void (*CuteQPixmapIconEngineCall0)(const void *, QPainter *, const QRect *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQPixmapIconEngineCall1)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQPixmapIconEngineCall2)(const void *, const QSize *, int, int, qreal, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QSize * (*CuteQPixmapIconEngineCall3)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQPixmapIconEngineCall4)(const void *, const QPixmap *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQPixmapIconEngineCall5)(const void *, const QString *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef bool (*CuteQPixmapIconEngineCall6)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQPixmapIconEngineCall7)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void * (*CuteQPixmapIconEngineCall8)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
typedef QString * (*CuteQPixmapIconEngineCall9)(const void *, int *);
class CuteQPixmapIconEngine : public QPixmapIconEngine {
public:
  using QPixmapIconEngine::QPixmapIconEngine;
  CuteQPixmapIconEngine(const QPixmapIconEngine &other) : QPixmapIconEngine(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine3keyEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine5cloneEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine8iconNameEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_ICON)
  //  void QPixmapIconEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(
      QPainter *painter,
      const QRect &rect,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapIconEngineCall0 call = reinterpret_cast<CuteQPixmapIconEngineCall0>(taken[0]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QPixmapIconEngine::paint(painter, rect, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QPixmapIconEngine::pixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapIconEngineCall1 call = reinterpret_cast<CuteQPixmapIconEngineCall1>(taken[1]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QPixmapIconEngine::pixmap(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QPixmapIconEngine::scaledPixmap(const QSize &size,
  //      QIcon::Mode mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapIconEngineCall2 call = reinterpret_cast<CuteQPixmapIconEngineCall2>(taken[2]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QPixmapIconEngine::scaledPixmap(size, mode, state, scale);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QSize QPixmapIconEngine::actualSize(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QSize actualSize(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapIconEngineCall3 call = reinterpret_cast<CuteQPixmapIconEngineCall3>(taken[3]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QPixmapIconEngine::actualSize(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QPixmapIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
  //      mode, QIcon::State state)
  void addPixmap(
      const QPixmap &pixmap,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapIconEngineCall4 call = reinterpret_cast<CuteQPixmapIconEngineCall4>(taken[4]);
      call(this, &pixmap, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QPixmapIconEngine::addPixmap(pixmap, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QPixmapIconEngine::addFile(const QString &fileName, const QSize
  //      &size, QIcon::Mode mode, QIcon::State state)
  void addFile(
      const QString &fileName,
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapIconEngineCall5 call = reinterpret_cast<CuteQPixmapIconEngineCall5>(taken[5]);
      call(this, &fileName, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QPixmapIconEngine::addFile(fileName, size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  bool QPixmapIconEngine::isNull()
  bool isNull() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPixmapIconEngineCall6 call = reinterpret_cast<CuteQPixmapIconEngineCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPixmapIconEngine::isNull();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QPixmapIconEngine::key() const
  QString key() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPixmapIconEngineCall7 call = reinterpret_cast<CuteQPixmapIconEngineCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPixmapIconEngine::key();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QIconEngine *QPixmapIconEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPixmapIconEngineCall8 call = reinterpret_cast<CuteQPixmapIconEngineCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QPixmapIconEngine::clone();
  }
#endif  // !defined(QT_NO_ICON)

  //  QString QIconEngine::iconName()
  QString iconName() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPixmapIconEngineCall9 call = reinterpret_cast<CuteQPixmapIconEngineCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QIconEngine::iconName();
  }
};

//  QPixmapIconEngine::QPixmapIconEngine()
extern "C" Q_DECL_EXPORT
QPixmapIconEngine *ritual_ZN17QPixmapIconEngineC1Ev() {
  return new CuteQPixmapIconEngine();
}

//  QPixmapIconEngine::QPixmapIconEngine(const QPixmapIconEngine &a0)
extern "C" Q_DECL_EXPORT
QPixmapIconEngine *ritual_ZN17QPixmapIconEngineC1ERKS_(
    const QPixmapIconEngine *a0) {
  return new CuteQPixmapIconEngine(*a0);
}

//  QPixmapIconEngine::~QPixmapIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapIconEngineD1Ev(QPixmapIconEngine *self) {
  delete self;
}

//  void QPixmapIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QPixmapIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QPixmap QPixmapIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN17QPixmapIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  QPixmap QPixmapIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN17QPixmapIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  QPixmapIconEngineEntry *QPixmapIconEngine::bestMatch(const QSize &size,
//      qreal scale, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN17QPixmapIconEngine9bestMatchERK5QSizedN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    qreal scale,
    QIcon::Mode mode,
    QIcon::State state) {
  return self->bestMatch(*size, scale, mode, state);
}

//  QSize QPixmapIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN17QPixmapIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QList<QSize> QPixmapIconEngine::availableSizes(QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN17QPixmapIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QPixmapIconEngine *self,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QList<QSize>(self->availableSizes(mode, state));
}

//  void QPixmapIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addPixmap(*pixmap, mode, state);
}

//  void QPixmapIconEngine::addFile(const QString &fileName, const QSize
//      &size, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QPixmapIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addFile(*fileName, *size, mode, state);
}

//  bool QPixmapIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPixmapIconEngine6isNullEv(QPixmapIconEngine *self) {
  return self->isNull();
}

//  QString QPixmapIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QPixmapIconEngine3keyEv(const QPixmapIconEngine *self) {
  return new QString(self->key());
}

//  QIconEngine *QPixmapIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK17QPixmapIconEngine5cloneEv(
    const QPixmapIconEngine *self) {
  return self->clone();
}

//  QSize QPixmapIconEngine::adjustSize(const QSize &expectedSize, QSize
//      size)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN17QPixmapIconEngine10adjustSizeERK5QSizeS0_(
    const QSize *expectedSize,
    const QSize *size) {
  return new QSize(QPixmapIconEngine::adjustSize(*expectedSize, *size));
}

//  void QPixmapIconEngine::removePixmapEntry(QPixmapIconEngineEntry *pe)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapIconEngine17removePixmapEntryEP22QPixmapIconEngineEntry(
    QPixmapIconEngine *self,
    QPixmapIconEngineEntry *pe) {
  self->removePixmapEntry(pe);
}

//  QPixmapIconEngineEntry *QPixmapIconEngine::tryMatch(const QSize &size,
//      qreal scale, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN17QPixmapIconEngine8tryMatchERK5QSizedN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    qreal scale,
    QIcon::Mode mode,
    QIcon::State state) {
  return self->tryMatch(*size, scale, mode, state);
}

//  a Python function taken by a CuteQPixmapIconEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapIconEngine(
    QPixmapIconEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapIconEngine *>(self)->take(key, call);
}

//  void QPixmapIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPixmapIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QPixmapIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QPixmapIconEngine::paint(painter, *rect, mode, state);
}

//  QPixmap QPixmapIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN17QPixmapIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QPixmapIconEngine::pixmap(*size, mode, state));
}

//  QPixmap QPixmapIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN17QPixmapIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(
      self->QPixmapIconEngine::scaledPixmap(
          *size,
          mode,
          state,
          scale));
}

//  QSize QPixmapIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN17QPixmapIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QPixmapIconEngine::actualSize(*size, mode, state));
}

//  void QPixmapIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPixmapIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QPixmapIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QPixmapIconEngine::addPixmap(*pixmap, mode, state);
}

//  void QPixmapIconEngine::addFile(const QString &fileName, const QSize
//      &size, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPixmapIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QPixmapIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QPixmapIconEngine::addFile(*fileName, *size, mode, state);
}

//  bool QPixmapIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPixmapIconEngine6isNullEv(QPixmapIconEngine *self) {
  return self->QPixmapIconEngine::isNull();
}

//  QString QPixmapIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QPixmapIconEngine3keyEv(
    const QPixmapIconEngine *self) {
  return new QString(self->QPixmapIconEngine::key());
}

//  QIconEngine *QPixmapIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK17QPixmapIconEngine5cloneEv(
    const QPixmapIconEngine *self) {
  return self->QPixmapIconEngine::clone();
}

#endif  // !defined(QT_NO_ICON)

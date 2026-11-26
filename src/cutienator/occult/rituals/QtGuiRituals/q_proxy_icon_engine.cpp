//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qiconengine.h>
#include <QtGui/private/qiconengine_p.h>
#include <QtGui/qpainter.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qiconengine.cpp, line 311, as _ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE
inline void QProxyIconEngine::paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->paint(painter, rect, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 316, as _ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE
inline QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->actualSize(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 321, as _ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE
inline QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->pixmap(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 326, as _ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE
inline void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addPixmap(pixmap, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 331, as _ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE
inline void QProxyIconEngine::addFile(const QString &fileName, const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addFile(fileName, size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 336, as _ZNK16QProxyIconEngine3keyEv
inline QString QProxyIconEngine::key() const
{
    return proxiedEngine()->key();
}

//  from src/gui/image/qiconengine.cpp, line 341, as _ZNK16QProxyIconEngine5cloneEv
inline QIconEngine *QProxyIconEngine::clone() const
{
    return proxiedEngine()->clone();
}

//  from src/gui/image/qiconengine.cpp, line 346, as _ZN16QProxyIconEngine4readER11QDataStream
inline bool QProxyIconEngine::read(QDataStream &in)
{
    return proxiedEngine()->read(in);
}

//  from src/gui/image/qiconengine.cpp, line 351, as _ZNK16QProxyIconEngine5writeER11QDataStream
inline bool QProxyIconEngine::write(QDataStream &out) const
{
    return proxiedEngine()->write(out);
}

//  from src/gui/image/qiconengine.cpp, line 356, as _ZN16QProxyIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE
inline QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->availableSizes(mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 361, as _ZN16QProxyIconEngine8iconNameEv
inline QString QProxyIconEngine::iconName()
{
    return proxiedEngine()->iconName();
}

//  from src/gui/image/qiconengine.cpp, line 366, as _ZN16QProxyIconEngine6isNullEv
inline bool QProxyIconEngine::isNull()
{
    return proxiedEngine()->isNull();
}

//  from src/gui/image/qiconengine.cpp, line 371, as _ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd
inline QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale)
{
    return proxiedEngine()->scaledPixmap(size, mode, state, scale);
}

//  from src/gui/image/qiconengine.cpp, line 376, as _ZN16QProxyIconEngine12virtual_hookEiPv
inline void QProxyIconEngine::virtual_hook(int id, void *data)
{
    proxiedEngine()->virtual_hook(id, data);
}
//  -----------------------------------------------------------------------

//  A QProxyIconEngine that Python can take functions over in. Every QProxyIconEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ICON)
typedef void (*CuteQProxyIconEngineCall0)(const void *, QPainter *, const QRect *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QSize * (*CuteQProxyIconEngineCall1)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQProxyIconEngineCall2)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQProxyIconEngineCall3)(const void *, const QPixmap *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQProxyIconEngineCall4)(const void *, const QString *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQProxyIconEngineCall5)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void * (*CuteQProxyIconEngineCall6)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQProxyIconEngineCall7)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef bool (*CuteQProxyIconEngineCall8)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQProxyIconEngineCall9)(const void *, const QSize *, int, int, qreal, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void (*CuteQProxyIconEngineCall10)(const void *, int, void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void * (*CuteQProxyIconEngineCall11)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
class CuteQProxyIconEngine : public QProxyIconEngine {
public:
  using QProxyIconEngine::QProxyIconEngine;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine3keyEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK11QIconEngine5cloneEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine8iconNameEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine12virtual_hookEiPv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZNK16QProxyIconEngine13proxiedEngineEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
    return false;
  }

#if !defined(QT_NO_ICON)
  //  void QProxyIconEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(
      QPainter *painter,
      const QRect &rect,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQProxyIconEngineCall0 call = reinterpret_cast<CuteQProxyIconEngineCall0>(taken[0]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QProxyIconEngine::paint(painter, rect, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QSize actualSize(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProxyIconEngineCall1 call = reinterpret_cast<CuteQProxyIconEngineCall1>(taken[1]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QProxyIconEngine::actualSize(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
  //      QIcon::State state)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQProxyIconEngineCall2 call = reinterpret_cast<CuteQProxyIconEngineCall2>(taken[2]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QProxyIconEngine::pixmap(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode
  //      mode, QIcon::State state)
  void addPixmap(
      const QPixmap &pixmap,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[3]) {
      int handled = 0;
      CuteQProxyIconEngineCall3 call = reinterpret_cast<CuteQProxyIconEngineCall3>(taken[3]);
      call(this, &pixmap, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QProxyIconEngine::addPixmap(pixmap, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QProxyIconEngine::addFile(const QString &fileName, const QSize
  //      &size, QIcon::Mode mode, QIcon::State state)
  void addFile(
      const QString &fileName,
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[4]) {
      int handled = 0;
      CuteQProxyIconEngineCall4 call = reinterpret_cast<CuteQProxyIconEngineCall4>(taken[4]);
      call(this, &fileName, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QProxyIconEngine::addFile(fileName, size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QProxyIconEngine::key() const
  QString key() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQProxyIconEngineCall5 call = reinterpret_cast<CuteQProxyIconEngineCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QProxyIconEngine::key();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QIconEngine *QProxyIconEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQProxyIconEngineCall6 call = reinterpret_cast<CuteQProxyIconEngineCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QProxyIconEngine::clone();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QProxyIconEngine::iconName()
  QString iconName() override {
    if (taken[7]) {
      int handled = 0;
      CuteQProxyIconEngineCall7 call = reinterpret_cast<CuteQProxyIconEngineCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QProxyIconEngine::iconName();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  bool QProxyIconEngine::isNull()
  bool isNull() override {
    if (taken[8]) {
      int handled = 0;
      CuteQProxyIconEngineCall8 call = reinterpret_cast<CuteQProxyIconEngineCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QProxyIconEngine::isNull();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[9]) {
      int handled = 0;
      CuteQProxyIconEngineCall9 call = reinterpret_cast<CuteQProxyIconEngineCall9>(taken[9]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QProxyIconEngine::scaledPixmap(size, mode, state, scale);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  void QProxyIconEngine::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[10]) {
      int handled = 0;
      CuteQProxyIconEngineCall10 call = reinterpret_cast<CuteQProxyIconEngineCall10>(taken[10]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QProxyIconEngine::virtual_hook(id, data);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QIconEngine *QProxyIconEngine::proxiedEngine() const
  QIconEngine *proxiedEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQProxyIconEngineCall11 call = reinterpret_cast<CuteQProxyIconEngineCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_ICON)
};

//  void QProxyIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QProxyIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addPixmap(*pixmap, mode, state);
}

//  void QProxyIconEngine::addFile(const QString &fileName, const QSize
//      &size, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QProxyIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addFile(*fileName, *size, mode, state);
}

//  QString QProxyIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QProxyIconEngine3keyEv(const QProxyIconEngine *self) {
  return new QString(self->key());
}

//  QIconEngine *QProxyIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QProxyIconEngine5cloneEv(
    const QProxyIconEngine *self) {
  return self->clone();
}

//  bool QProxyIconEngine::read(QDataStream &in)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProxyIconEngine4readER11QDataStream(
    QProxyIconEngine *self,
    QDataStream *in) {
  return self->read(*in);
}

//  bool QProxyIconEngine::write(QDataStream &out) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QProxyIconEngine5writeER11QDataStream(
    const QProxyIconEngine *self,
    QDataStream *out) {
  return self->write(*out);
}

//  QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN16QProxyIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QProxyIconEngine *self,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QList<QSize>(self->availableSizes(mode, state));
}

//  QString QProxyIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QProxyIconEngine8iconNameEv(QProxyIconEngine *self) {
  return new QString(self->iconName());
}

//  bool QProxyIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProxyIconEngine6isNullEv(QProxyIconEngine *self) {
  return self->isNull();
}

//  QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  void QProxyIconEngine::virtual_hook(int id, void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProxyIconEngine12virtual_hookEiPv(
    QProxyIconEngine *self,
    int id,
    void *data) {
  self->virtual_hook(id, data);
}

//  QIconEngine *QProxyIconEngine::proxiedEngine() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QProxyIconEngine13proxiedEngineEv(
    const QProxyIconEngine *self) {
  return self->proxiedEngine();
}

//  a Python function taken by a CuteQProxyIconEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProxyIconEngine(
    QProxyIconEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProxyIconEngine *>(self)->take(key, call);
}

//  void QProxyIconEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QProxyIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QProxyIconEngine::paint(painter, *rect, mode, state);
}

//  QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QProxyIconEngine::actualSize(*size, mode, state));
}

//  QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QProxyIconEngine::pixmap(*size, mode, state));
}

//  void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QProxyIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QProxyIconEngine::addPixmap(*pixmap, mode, state);
}

//  void QProxyIconEngine::addFile(const QString &fileName, const QSize
//      &size, QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QProxyIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QProxyIconEngine::addFile(*fileName, *size, mode, state);
}

//  QString QProxyIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QProxyIconEngine3keyEv(
    const QProxyIconEngine *self) {
  return new QString(self->QProxyIconEngine::key());
}

//  QIconEngine *QProxyIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK16QProxyIconEngine5cloneEv(
    const QProxyIconEngine *self) {
  return self->QProxyIconEngine::clone();
}

//  QString QProxyIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN16QProxyIconEngine8iconNameEv(QProxyIconEngine *self) {
  return new QString(self->QProxyIconEngine::iconName());
}

//  bool QProxyIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QProxyIconEngine6isNullEv(QProxyIconEngine *self) {
  return self->QProxyIconEngine::isNull();
}

//  QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QProxyIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(
      self->QProxyIconEngine::scaledPixmap(
          *size,
          mode,
          state,
          scale));
}

//  void QProxyIconEngine::virtual_hook(int id, void *data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QProxyIconEngine12virtual_hookEiPv(
    QProxyIconEngine *self,
    int id,
    void *data) {
  self->QProxyIconEngine::virtual_hook(id, data);
}

#endif  // !defined(QT_NO_ICON)

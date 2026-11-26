//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef QT_NO_ICON
#include <QtGui/private/qiconloader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qicon_p.h>
#include <QtGui/QIconEnginePlugin>
#include <QtGui/QPixmapCache>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qfontdatabase.h>
#include <QtGui/QPalette>
#include <QtCore/qmath.h>
#include <QtCore/QList>
#include <QtCore/QDir>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(settings)
#include <QtCore/QSettings>
#endif
#include <QtGui/QPainter>
#include <QtGui/private/qhexstring_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtGui/private/qfonticonengine_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/image/qiconloader.cpp, line 912, as _ZN17QIconLoaderEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE
#if !defined(QT_NO_ICON)
inline QSize QIconLoaderEngine::actualSize(const QSize &size, QIcon::Mode mode,
                                   QIcon::State state)
{
    Q_UNUSED(mode);
    Q_UNUSED(state);

    QIconLoaderEngineEntry *entry = entryForSize(m_info, size);
    if (entry) {
        const QIconDirInfo &dir = entry->dir;
        if (dir.type == QIconDirInfo::Scalable) {
            return size;
        } else if (dir.type == QIconDirInfo::Fallback) {
            return QIcon(entry->filename).actualSize(size, mode, state);
        } else {
            int result = qMin<int>(dir.size * dir.scale, qMin(size.width(), size.height()));
            return QSize(result, result);
        }
    }
    return QSize(0, 0);
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 999, as _ZN17QIconLoaderEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd
#if !defined(QT_NO_ICON)
inline QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale)
{
    const int integerScale = qCeil(scale);
    QIconLoaderEngineEntry *entry = entryForSize(m_info, size, integerScale);
    return entry ? entry->pixmap(size, mode, state, scale) : QPixmap();
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 1006, as _ZN17QIconLoaderEngine14availableSizesEN5QIcon4ModeENS0_5StateE
#if !defined(QT_NO_ICON)
inline QList<QSize> QIconLoaderEngine::availableSizes(QIcon::Mode mode, QIcon::State state)
{
    Q_UNUSED(mode);
    Q_UNUSED(state);

    const qsizetype N = qsizetype(m_info.entries.size());
    QList<QSize> sizes;
    sizes.reserve(N);

    // Gets all sizes from the DirectoryInfo entries
    for (const auto &entry : m_info.entries) {
        if (entry->dir.type == QIconDirInfo::Fallback) {
            sizes.append(QIcon(entry->filename).availableSizes());
        } else {
            int size = entry->dir.size;
            sizes.append(QSize(size, size));
        }
    }
    return sizes;
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 803, as _ZN17QIconLoaderEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE
#if !defined(QT_NO_ICON)
inline void QIconLoaderEngine::paint(QPainter *painter, const QRect &rect,
                             QIcon::Mode mode, QIcon::State state)
{
    const auto dpr = painter->device()->devicePixelRatio();
    painter->drawPixmap(rect, scaledPixmap(rect.size(), mode, state, dpr));
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 994, as _ZN17QIconLoaderEngine6isNullEv
#if !defined(QT_NO_ICON)
inline bool QIconLoaderEngine::isNull()
{
    return m_info.entries.empty();
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 978, as _ZN17QIconLoaderEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE
#if !defined(QT_NO_ICON)
inline QPixmap QIconLoaderEngine::pixmap(const QSize &size, QIcon::Mode mode,
                                 QIcon::State state)
{
    return scaledPixmap(size, mode, state, 1.0);
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 989, as _ZN17QIconLoaderEngine8iconNameEv
#if !defined(QT_NO_ICON)
inline QString QIconLoaderEngine::iconName()
{
    return m_info.iconName;
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 984, as _ZNK17QIconLoaderEngine3keyEv
#if !defined(QT_NO_ICON)
inline QString QIconLoaderEngine::key() const
{
    return u"QIconLoaderEngine"_s;
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 792, as _ZNK17QIconLoaderEngine5cloneEv
#if !defined(QT_NO_ICON)
inline QIconEngine *QIconLoaderEngine::clone() const
{
    Q_UNREACHABLE();
    return nullptr; // Cannot be cloned
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 784, as _ZN17QIconLoaderEngineC1ERK7QString
#if !defined(QT_NO_ICON)
inline QIconLoaderEngine::QIconLoaderEngine(const QString& iconName)
    : m_iconName(iconName)
    , m_info(QIconLoader::instance()->loadIcon(m_iconName))
{
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 790, as _ZN17QIconLoaderEngineD1Ev
#if !defined(QT_NO_ICON)
inline QIconLoaderEngine::~QIconLoaderEngine() = default;
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 798, as _ZNK17QIconLoaderEngine7hasIconEv
#if !defined(QT_NO_ICON)
inline bool QIconLoaderEngine::hasIcon() const
{
    return !(m_info.entries.empty());
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

//  A QIconLoaderEngine that Python can take functions over in. Every QIconLoaderEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ICON)
typedef void (*CuteQIconLoaderEngineCall0)(const void *, QPainter *, const QRect *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQIconLoaderEngineCall1)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QSize * (*CuteQIconLoaderEngineCall2)(const void *, const QSize *, int, int, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef void * (*CuteQIconLoaderEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQIconLoaderEngineCall4)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef bool (*CuteQIconLoaderEngineCall5)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQIconLoaderEngineCall6)(const void *, const QSize *, int, int, qreal, int *);
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
typedef QString * (*CuteQIconLoaderEngineCall7)(const void *, int *);
#endif  // !defined(QT_NO_ICON)
typedef void (*CuteQIconLoaderEngineCall8)(const void *, const QPixmap *, int, int, int *);
typedef void (*CuteQIconLoaderEngineCall9)(const void *, const QString *, const QSize *, int, int, int *);
typedef void (*CuteQIconLoaderEngineCall10)(const void *, int, void *, int *);
class CuteQIconLoaderEngine : public QIconLoaderEngine {
public:
  using QIconLoaderEngine::QIconLoaderEngine;
  void *taken[11] = {};

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
    if (!std::strcmp(key, "_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE")) {
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
    if (!std::strcmp(key, "_ZN11QIconEngine8iconNameEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine6isNullEv")) {
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
    if (!std::strcmp(key, "_ZNK11QIconEngine3keyEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QIconEngine12virtual_hookEiPv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_ICON)
  //  void QIconLoaderEngine::paint(QPainter *painter, const QRect &rect,
  //      QIcon::Mode mode, QIcon::State state)
  void paint(
      QPainter *painter,
      const QRect &rect,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconLoaderEngineCall0 call = reinterpret_cast<CuteQIconLoaderEngineCall0>(taken[0]);
      call(this, painter, &rect, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconLoaderEngine::paint(painter, rect, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QIconLoaderEngine::pixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconLoaderEngineCall1 call = reinterpret_cast<CuteQIconLoaderEngineCall1>(taken[1]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QIconLoaderEngine::pixmap(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QSize QIconLoaderEngine::actualSize(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state)
  QSize actualSize(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQIconLoaderEngineCall2 call = reinterpret_cast<CuteQIconLoaderEngineCall2>(taken[2]);
      const QSize * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled && given) return *given;
    }
    return QIconLoaderEngine::actualSize(size, mode, state);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QIconEngine *QIconLoaderEngine::clone() const
  QIconEngine *clone() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQIconLoaderEngineCall3 call = reinterpret_cast<CuteQIconLoaderEngineCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconEngine *>(given);
    }
    return QIconLoaderEngine::clone();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QIconLoaderEngine::iconName()
  QString iconName() override {
    if (taken[4]) {
      int handled = 0;
      CuteQIconLoaderEngineCall4 call = reinterpret_cast<CuteQIconLoaderEngineCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QIconLoaderEngine::iconName();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  bool QIconLoaderEngine::isNull()
  bool isNull() override {
    if (taken[5]) {
      int handled = 0;
      CuteQIconLoaderEngineCall5 call = reinterpret_cast<CuteQIconLoaderEngineCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIconLoaderEngine::isNull();
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size,
  //      QIcon::Mode mode, QIcon::State state, qreal scale)
  QPixmap scaledPixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[6]) {
      int handled = 0;
      CuteQIconLoaderEngineCall6 call = reinterpret_cast<CuteQIconLoaderEngineCall6>(taken[6]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return QIconLoaderEngine::scaledPixmap(size, mode, state, scale);
  }
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
  //  QString QIconLoaderEngine::key() const
  QString key() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQIconLoaderEngineCall7 call = reinterpret_cast<CuteQIconLoaderEngineCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QIconLoaderEngine::key();
  }
#endif  // !defined(QT_NO_ICON)

  //  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
  //      QIcon::State state)
  void addPixmap(
      const QPixmap &pixmap,
      QIcon::Mode mode,
      QIcon::State state) override {
    if (taken[8]) {
      int handled = 0;
      CuteQIconLoaderEngineCall8 call = reinterpret_cast<CuteQIconLoaderEngineCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQIconLoaderEngineCall9 call = reinterpret_cast<CuteQIconLoaderEngineCall9>(taken[9]);
      call(this, &fileName, &size, static_cast<int>(mode), static_cast<int>(state), &handled);
      if (handled) return;
    }
    QIconEngine::addFile(fileName, size, mode, state);
  }

  //  void QIconEngine::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[10]) {
      int handled = 0;
      CuteQIconLoaderEngineCall10 call = reinterpret_cast<CuteQIconLoaderEngineCall10>(taken[10]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QIconEngine::virtual_hook(id, data);
  }
};

#if !defined(QT_NO_ICON)
//  QIconLoaderEngine::QIconLoaderEngine(const QString &iconName)
extern "C" Q_DECL_EXPORT
QIconLoaderEngine *ritual_ZN17QIconLoaderEngineC1ERK7QString(
    const QString *iconName) {
  return new CuteQIconLoaderEngine(*iconName);
}
#endif  // !defined(QT_NO_ICON)

//  QIconLoaderEngine::~QIconLoaderEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconLoaderEngineD1Ev(QIconLoaderEngine *self) {
  delete self;
}

//  void QIconLoaderEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconLoaderEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QIconLoaderEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QPixmap QIconLoaderEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN17QIconLoaderEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  QSize QIconLoaderEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN17QIconLoaderEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QIconEngine *QIconLoaderEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK17QIconLoaderEngine5cloneEv(
    const QIconLoaderEngine *self) {
  return self->clone();
}

//  QString QIconLoaderEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QIconLoaderEngine8iconNameEv(QIconLoaderEngine *self) {
  return new QString(self->iconName());
}

//  bool QIconLoaderEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconLoaderEngine6isNullEv(QIconLoaderEngine *self) {
  return self->isNull();
}

//  QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN17QIconLoaderEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}

//  QList<QSize> QIconLoaderEngine::availableSizes(QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN17QIconLoaderEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QIconLoaderEngine *self,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QList<QSize>(self->availableSizes(mode, state));
}

//  QIconLoaderEngineEntry *QIconLoaderEngine::entryForSize(const
//      QThemeIconInfo &info, const QSize &size, int scale)
extern "C" Q_DECL_EXPORT
QIconLoaderEngineEntry *ritual_ZN17QIconLoaderEngine12entryForSizeERK14QThemeIconInfoRK5QSizei(
    const QThemeIconInfo *info,
    const QSize *size,
    int scale) {
  return QIconLoaderEngine::entryForSize(*info, *size, scale);
}

//  QString QIconLoaderEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QIconLoaderEngine3keyEv(const QIconLoaderEngine *self) {
  return new QString(self->key());
}

#if !defined(QT_NO_ICON)
//  bool QIconLoaderEngine::hasIcon() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QIconLoaderEngine7hasIconEv(const QIconLoaderEngine *self) {
  return self->hasIcon();
}
#endif  // !defined(QT_NO_ICON)

//  a Python function taken by a CuteQIconLoaderEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconLoaderEngine(
    QIconLoaderEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconLoaderEngine *>(self)->take(key, call);
}

#if !defined(QT_NO_ICON)
//  void QIconLoaderEngine::paint(QPainter *painter, const QRect &rect,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconLoaderEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QIconLoaderEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->QIconLoaderEngine::paint(painter, *rect, mode, state);
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QPixmap QIconLoaderEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN17QIconLoaderEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->QIconLoaderEngine::pixmap(*size, mode, state));
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QSize QIconLoaderEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN17QIconLoaderEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->QIconLoaderEngine::actualSize(*size, mode, state));
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QIconEngine *QIconLoaderEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_own_ZNK17QIconLoaderEngine5cloneEv(
    const QIconLoaderEngine *self) {
  return self->QIconLoaderEngine::clone();
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QString QIconLoaderEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN17QIconLoaderEngine8iconNameEv(
    QIconLoaderEngine *self) {
  return new QString(self->QIconLoaderEngine::iconName());
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  bool QIconLoaderEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconLoaderEngine6isNullEv(QIconLoaderEngine *self) {
  return self->QIconLoaderEngine::isNull();
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QPixmap QIconLoaderEngine::scaledPixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN17QIconLoaderEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconLoaderEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(
      self->QIconLoaderEngine::scaledPixmap(
          *size,
          mode,
          state,
          scale));
}
#endif  // !defined(QT_NO_ICON)

#if !defined(QT_NO_ICON)
//  QString QIconLoaderEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QIconLoaderEngine3keyEv(
    const QIconLoaderEngine *self) {
  return new QString(self->QIconLoaderEngine::key());
}
#endif  // !defined(QT_NO_ICON)

#endif  // !defined(QT_NO_ICON)

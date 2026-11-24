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
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  A QIconLoaderEngineEntry that Python can take functions over in. Every QIconLoaderEngineEntry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ICON)
typedef const QPixmap * (*CuteQIconLoaderEngineEntryCall0)(const void *, const QSize *, int, int, qreal, int *);
#endif  // !defined(QT_NO_ICON)
class CuteQIconLoaderEngineEntry : public QIconLoaderEngineEntry {
public:
  using QIconLoaderEngineEntry::QIconLoaderEngineEntry;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ICON)
    if (!std::strcmp(key, "_ZN22QIconLoaderEngineEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_ICON)
    return false;
  }

#if !defined(QT_NO_ICON)
  //  QPixmap QIconLoaderEngineEntry::pixmap(const QSize &size, QIcon::Mode
  //      mode, QIcon::State state, qreal scale)
  QPixmap pixmap(
      const QSize &size,
      QIcon::Mode mode,
      QIcon::State state,
      qreal scale) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconLoaderEngineEntryCall0 call = reinterpret_cast<CuteQIconLoaderEngineEntryCall0>(taken[0]);
      const QPixmap * given = call(this, &size, static_cast<int>(mode), static_cast<int>(state), scale, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_ICON)
};

//  QIconLoaderEngineEntry::~QIconLoaderEngineEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QIconLoaderEngineEntryD1Ev(QIconLoaderEngineEntry *self) {
  delete self;
}

//  QPixmap QIconLoaderEngineEntry::pixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN22QIconLoaderEngineEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconLoaderEngineEntry *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->pixmap(*size, mode, state, scale));
}

//  a Python function taken by a CuteQIconLoaderEngineEntry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconLoaderEngineEntry(
    QIconLoaderEngineEntry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconLoaderEngineEntry *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_ICON)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutstyleinfo_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-27: code taken from Qt's source no
//  longer stands under defined(Q_OS_LINUX), which Qt does not write there;
//  its rituals no longer stand under defined(Q_OS_LINUX), as the code taken
//  from Qt they call no longer does. Kept as it is when the generator runs
//  again.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutstyleinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qfont_p.h>
#include <QtQuickLayouts/private/qquicklayoutstyleinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutstyleinfo.cpp, line 33, as _ZNK21QQuickLayoutStyleInfo12windowMarginEN2Qt11OrientationE
inline qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation /*orientation*/) const
{
    return 0;
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutstyleinfo.cpp, line 38, as _ZNK21QQuickLayoutStyleInfo14hasChangedCoreEv
inline bool QQuickLayoutStyleInfo::hasChangedCore() const
{
    // never changes
    return false;
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutstyleinfo.cpp, line 16, as _ZNK21QQuickLayoutStyleInfo7spacingEN2Qt11OrientationE
inline qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation /*orientation*/) const
{
#if defined(Q_OS_ANDROID) || defined(Q_OS_IOS) || defined(Q_OS_QNX)
    // On Android and iOS the default spacing between each UI element is 8dp
    qreal spacing = 8.0;
#else
    qreal spacing = 5.0;
#endif

#ifndef Q_OS_MACOS
    // On OS X the DPI is always 72 so we should not scale it
    spacing = qRound(spacing * (qreal(qt_defaultDpiX()) / 96.0));
#endif

    return spacing;
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutstyleinfo.cpp, line 12, as _ZN21QQuickLayoutStyleInfoC1Ev
inline QQuickLayoutStyleInfo::QQuickLayoutStyleInfo()
{
}
//  -----------------------------------------------------------------------

//  A QQuickLayoutStyleInfo that Python can take functions over in. Every QQuickLayoutStyleInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickLayoutStyleInfoCall0)(const void *, int, int *);
typedef qreal (*CuteQQuickLayoutStyleInfoCall1)(const void *, int, int *);
typedef bool (*CuteQQuickLayoutStyleInfoCall2)(const void *, int *);
typedef qreal (*CuteQQuickLayoutStyleInfoCall3)(const void *, int, int, int, int *);
typedef qreal (*CuteQQuickLayoutStyleInfoCall4)(const void *, int, int, int, int *);
typedef void (*CuteQQuickLayoutStyleInfoCall5)(const void *, int *);
class CuteQQuickLayoutStyleInfo : public QQuickLayoutStyleInfo {
public:
  using QQuickLayoutStyleInfo::QQuickLayoutStyleInfo;
  CuteQQuickLayoutStyleInfo(const QQuickLayoutStyleInfo & other) : QQuickLayoutStyleInfo(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11OrientationE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractLayoutStyleInfo10invalidateEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation orientation)
  //      const
  qreal spacing(Qt::Orientation orientation) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall0 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall0>(taken[0]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QQuickLayoutStyleInfo::spacing(orientation);
  }

  //  qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation
  //      orientation) const
  qreal windowMargin(Qt::Orientation orientation) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall1 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall1>(taken[1]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QQuickLayoutStyleInfo::windowMargin(orientation);
  }

  //  bool QQuickLayoutStyleInfo::hasChangedCore() const
  bool hasChangedCore() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall2 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickLayoutStyleInfo::hasChangedCore();
  }

  //  qreal QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
  //      ControlTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation
  //      a2) const
  qreal combinedLayoutSpacing(
      QLayoutPolicy::ControlTypes a0,
      QLayoutPolicy::ControlTypes a1,
      Qt::Orientation a2) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall3 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall3>(taken[3]);
      qreal given = call(this, static_cast<int>(a0.toInt()), static_cast<int>(a1.toInt()), static_cast<int>(a2), &handled);
      if (handled) return given;
    }
    return QAbstractLayoutStyleInfo::combinedLayoutSpacing(a0, a1, a2);
  }

  //  qreal
  //      QAbstractLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlTy
  //      pe a0, QLayoutPolicy::ControlType a1, Qt::Orientation a2) const
  qreal perItemSpacing(
      QLayoutPolicy::ControlType a0,
      QLayoutPolicy::ControlType a1,
      Qt::Orientation a2) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall4 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall4>(taken[4]);
      qreal given = call(this, static_cast<int>(a0), static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return given;
    }
    return QAbstractLayoutStyleInfo::perItemSpacing(a0, a1, a2);
  }

  //  void QAbstractLayoutStyleInfo::invalidate()
  void invalidate() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLayoutStyleInfoCall5 call = reinterpret_cast<CuteQQuickLayoutStyleInfoCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractLayoutStyleInfo::invalidate();
  }
};

//  QQuickLayoutStyleInfo::QQuickLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
QQuickLayoutStyleInfo *ritual_ZN21QQuickLayoutStyleInfoC1Ev() {
  return new CuteQQuickLayoutStyleInfo();
}

//  qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickLayoutStyleInfo7spacingEN2Qt11OrientationE(
    const QQuickLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->spacing(orientation);
}

//  qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickLayoutStyleInfo12windowMarginEN2Qt11OrientationE(
    const QQuickLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->windowMargin(orientation);
}

//  bool QQuickLayoutStyleInfo::hasChangedCore() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickLayoutStyleInfo14hasChangedCoreEv(
    const QQuickLayoutStyleInfo *self) {
  return self->hasChangedCore();
}

//  QQuickLayoutStyleInfo::~QQuickLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutStyleInfoD1Ev(QQuickLayoutStyleInfo *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickLayoutStyleInfo, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLayoutStyleInfo(
    QQuickLayoutStyleInfo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLayoutStyleInfo *>(self)->take(key, call);
}

//  qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QQuickLayoutStyleInfo7spacingEN2Qt11OrientationE(
    const QQuickLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->QQuickLayoutStyleInfo::spacing(orientation);
}

//  qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QQuickLayoutStyleInfo12windowMarginEN2Qt11OrientationE(
    const QQuickLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->QQuickLayoutStyleInfo::windowMargin(orientation);
}

//  bool QQuickLayoutStyleInfo::hasChangedCore() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QQuickLayoutStyleInfo14hasChangedCoreEv(
    const QQuickLayoutStyleInfo *self) {
  return self->QQuickLayoutStyleInfo::hasChangedCore();
}

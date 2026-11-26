//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qabstractlayoutstyleinfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qabstractlayoutstyleinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QAbstractLayoutStyleInfo that Python can take functions over in. Every QAbstractLayoutStyleInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQAbstractLayoutStyleInfoCall0)(const void *, int, int, int, int *);
typedef qreal (*CuteQAbstractLayoutStyleInfoCall1)(const void *, int, int, int, int *);
typedef qreal (*CuteQAbstractLayoutStyleInfoCall2)(const void *, int, int *);
typedef bool (*CuteQAbstractLayoutStyleInfoCall3)(const void *, int *);
typedef void (*CuteQAbstractLayoutStyleInfoCall4)(const void *, int *);
typedef qreal (*CuteQAbstractLayoutStyleInfoCall5)(const void *, int, int *);
class CuteQAbstractLayoutStyleInfo : public QAbstractLayoutStyleInfo {
public:
  using QAbstractLayoutStyleInfo::QAbstractLayoutStyleInfo;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractLayoutStyleInfo10invalidateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11OrientationE")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  qreal QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
  //      ControlTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation
  //      a2) const
  qreal combinedLayoutSpacing(
      QLayoutPolicy::ControlTypes a0,
      QLayoutPolicy::ControlTypes a1,
      Qt::Orientation a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall0 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall1 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall1>(taken[1]);
      qreal given = call(this, static_cast<int>(a0), static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return given;
    }
    return QAbstractLayoutStyleInfo::perItemSpacing(a0, a1, a2);
  }

  //  qreal QAbstractLayoutStyleInfo::spacing(Qt::Orientation orientation)
  //      const
  qreal spacing(Qt::Orientation orientation) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall2 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall2>(taken[2]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAbstractLayoutStyleInfo::hasChangedCore() const
  bool hasChangedCore() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall3 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractLayoutStyleInfo::hasChangedCore();
  }

  //  void QAbstractLayoutStyleInfo::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall4 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractLayoutStyleInfo::invalidate();
  }

  //  qreal QAbstractLayoutStyleInfo::windowMargin(Qt::Orientation
  //      orientation) const
  qreal windowMargin(Qt::Orientation orientation) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractLayoutStyleInfoCall5 call = reinterpret_cast<CuteQAbstractLayoutStyleInfoCall5>(taken[5]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QAbstractLayoutStyleInfo::QAbstractLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
QAbstractLayoutStyleInfo *ritual_ZN24QAbstractLayoutStyleInfoC1Ev() {
  return new CuteQAbstractLayoutStyleInfo();
}

//  QAbstractLayoutStyleInfo::~QAbstractLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractLayoutStyleInfoD1Ev(
    QAbstractLayoutStyleInfo *self) {
  delete self;
}

//  qreal QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::Cont
//      rolTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation a2)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    int a0,
    int a1,
    Qt::Orientation a2) {
  return self->combinedLayoutSpacing(
      QFlags<QLayoutPolicy::ControlType>::fromInt(a0),
      QFlags<QLayoutPolicy::ControlType>::fromInt(a1),
      a2);
}

//  qreal QAbstractLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType
//      a0, QLayoutPolicy::ControlType a1, Qt::Orientation a2) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    QLayoutPolicy::ControlType a0,
    QLayoutPolicy::ControlType a1,
    Qt::Orientation a2) {
  return self->perItemSpacing(a0, a1, a2);
}

//  qreal QAbstractLayoutStyleInfo::spacing(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->spacing(orientation);
}

//  bool QAbstractLayoutStyleInfo::hasChangedCore() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv(
    const QAbstractLayoutStyleInfo *self) {
  return self->hasChangedCore();
}

//  void QAbstractLayoutStyleInfo::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractLayoutStyleInfo10invalidateEv(
    QAbstractLayoutStyleInfo *self) {
  self->invalidate();
}

//  qreal QAbstractLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->windowMargin(orientation);
}

//  bool QAbstractLayoutStyleInfo::isWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractLayoutStyleInfo8isWindowEv(
    const QAbstractLayoutStyleInfo *self) {
  return self->isWindow();
}

//  a Python function taken by a CuteQAbstractLayoutStyleInfo, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractLayoutStyleInfo(
    QAbstractLayoutStyleInfo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractLayoutStyleInfo *>(self)->take(key, call);
}

//  qreal QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::Cont
//      rolTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation a2)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    int a0,
    int a1,
    Qt::Orientation a2) {
  return self->QAbstractLayoutStyleInfo::combinedLayoutSpacing(
      QFlags<QLayoutPolicy::ControlType>::fromInt(a0),
      QFlags<QLayoutPolicy::ControlType>::fromInt(a1),
      a2);
}

//  qreal QAbstractLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType
//      a0, QLayoutPolicy::ControlType a1, Qt::Orientation a2) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE(
    const QAbstractLayoutStyleInfo *self,
    QLayoutPolicy::ControlType a0,
    QLayoutPolicy::ControlType a1,
    Qt::Orientation a2) {
  return self->QAbstractLayoutStyleInfo::perItemSpacing(a0, a1, a2);
}

//  bool QAbstractLayoutStyleInfo::hasChangedCore() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv(
    const QAbstractLayoutStyleInfo *self) {
  return self->QAbstractLayoutStyleInfo::hasChangedCore();
}

//  void QAbstractLayoutStyleInfo::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractLayoutStyleInfo10invalidateEv(
    QAbstractLayoutStyleInfo *self) {
  self->QAbstractLayoutStyleInfo::invalidate();
}

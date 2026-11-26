//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/infinitegrid_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/infinitegrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DInfiniteGrid that Python can take functions over in. Every QQuick3DInfiniteGrid
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DInfiniteGridCall0)(const void *, int *);
typedef void (*CuteQQuick3DInfiniteGridCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInfiniteGridCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInfiniteGridCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInfiniteGridCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInfiniteGridCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInfiniteGridCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInfiniteGridCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInfiniteGridCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DInfiniteGrid : public QQuick3DInfiniteGrid {
public:
  using QQuick3DInfiniteGrid::QQuick3DInfiniteGrid;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DInfiniteGrid::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall0 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DInfiniteGrid::componentComplete();
  }

  //  void QQuick3DInfiniteGrid::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall1 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DInfiniteGrid::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall2 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall3 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall4 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall5 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall6 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall7 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DInfiniteGridCall8 call = reinterpret_cast<CuteQQuick3DInfiniteGridCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DInfiniteGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DInfiniteGrid10metaObjectEv(
    const QQuick3DInfiniteGrid *self) {
  return self->metaObject();
}

//  void *QQuick3DInfiniteGrid::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DInfiniteGrid11qt_metacastEPKc(
    QQuick3DInfiniteGrid *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DInfiniteGrid::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DInfiniteGrid11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DInfiniteGrid *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DInfiniteGrid::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuick3DInfiniteGrid2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DInfiniteGrid::tr(s, c, n));
}

//  QQuick3DInfiniteGrid::QQuick3DInfiniteGrid()
extern "C" Q_DECL_EXPORT
QQuick3DInfiniteGrid *ritual_ZN20QQuick3DInfiniteGridC1Ev() {
  return new CuteQQuick3DInfiniteGrid();
}

//  QQuick3DInfiniteGrid::~QQuick3DInfiniteGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGridD1Ev(QQuick3DInfiniteGrid *self) {
  delete self;
}

//  bool QQuick3DInfiniteGrid::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuick3DInfiniteGrid7visibleEv(
    const QQuick3DInfiniteGrid *self) {
  return self->visible();
}

//  void QQuick3DInfiniteGrid::setVisible(bool newVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid10setVisibleEb(
    QQuick3DInfiniteGrid *self,
    bool newVisible) {
  self->setVisible(newVisible);
}

//  float QQuick3DInfiniteGrid::gridInterval() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DInfiniteGrid12gridIntervalEv(
    const QQuick3DInfiniteGrid *self) {
  return self->gridInterval();
}

//  void QQuick3DInfiniteGrid::setGridInterval(float newGridInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid15setGridIntervalEf(
    QQuick3DInfiniteGrid *self,
    float newGridInterval) {
  self->setGridInterval(newGridInterval);
}

//  void QQuick3DInfiniteGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid17componentCompleteEv(
    QQuick3DInfiniteGrid *self) {
  self->componentComplete();
}

//  void QQuick3DInfiniteGrid::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid10classBeginEv(
    QQuick3DInfiniteGrid *self) {
  self->classBegin();
}

//  bool QQuick3DInfiniteGrid::gridAxes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuick3DInfiniteGrid8gridAxesEv(
    const QQuick3DInfiniteGrid *self) {
  return self->gridAxes();
}

//  void QQuick3DInfiniteGrid::setGridAxes(bool newGridAxes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid11setGridAxesEb(
    QQuick3DInfiniteGrid *self,
    bool newGridAxes) {
  self->setGridAxes(newGridAxes);
}

//  void QQuick3DInfiniteGrid::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid14visibleChangedEv(
    QQuick3DInfiniteGrid *self) {
  self->visibleChanged();
}

//  void QQuick3DInfiniteGrid::gridIntervalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid19gridIntervalChangedEv(
    QQuick3DInfiniteGrid *self) {
  self->gridIntervalChanged();
}

//  void QQuick3DInfiniteGrid::gridAxesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid15gridAxesChangedEv(
    QQuick3DInfiniteGrid *self) {
  self->gridAxesChanged();
}

//  void QQuick3DInfiniteGrid::updateGridFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DInfiniteGrid15updateGridFlagsEv(
    QQuick3DInfiniteGrid *self) {
  self->updateGridFlags();
}

//  QQuick3DInfiniteGrid as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DInfiniteGrid_QQmlParserStatus(
    QQuick3DInfiniteGrid *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DInfiniteGrid, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DInfiniteGrid(
    QQuick3DInfiniteGrid *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DInfiniteGrid *>(self)->take(key, call);
}

//  void QQuick3DInfiniteGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuick3DInfiniteGrid17componentCompleteEv(
    QQuick3DInfiniteGrid *self) {
  self->QQuick3DInfiniteGrid::componentComplete();
}

//  void QQuick3DInfiniteGrid::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuick3DInfiniteGrid10classBeginEv(
    QQuick3DInfiniteGrid *self) {
  self->QQuick3DInfiniteGrid::classBegin();
}

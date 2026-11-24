//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
#if QT_CONFIG(animation)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTreeViewPrivate::AnimatedOperation that Python can take functions over in. Every QTreeViewPrivate::AnimatedOperation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall0)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteQTreeViewPrivate_AnimatedOperationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQTreeViewPrivate_AnimatedOperationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQTreeViewPrivate_AnimatedOperationCall5)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTreeViewPrivate_AnimatedOperationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewPrivate_AnimatedOperationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTreeViewPrivate_AnimatedOperation : public QTreeViewPrivate::AnimatedOperation {
public:
  using QTreeViewPrivate::AnimatedOperation::AnimatedOperation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::AnimatedOperation::updateCurrentValue(const
  //      QVariant &a0)
  void updateCurrentValue(const QVariant &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall0 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QTreeViewPrivate::AnimatedOperation::updateCurrentValue(a0);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::AnimatedOperation::updateState(State state,
  //      State a1)
  void updateState(
      QAbstractAnimation::State state,
      QAbstractAnimation::State a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall1 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall1>(taken[1]);
      call(this, static_cast<int>(state), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QTreeViewPrivate::AnimatedOperation::updateState(state, a1);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall2 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QVariantAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall3 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall4 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  QVariant QVariantAnimation::interpolated(const QVariant &from, const
  //      QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall5 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall5>(taken[5]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return QVariantAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall6 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall6>(taken[6]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall7 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall8 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall9 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall10 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall11 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTreeViewPrivate_AnimatedOperationCall12 call = reinterpret_cast<CuteQTreeViewPrivate_AnimatedOperationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QTreeViewPrivate::AnimatedOperation::AnimatedOperation()
extern "C" Q_DECL_EXPORT
QTreeViewPrivate::AnimatedOperation *ritual_ZN16QTreeViewPrivate17AnimatedOperationC1Ev() {
  return new CuteQTreeViewPrivate_AnimatedOperation();
}

//  int QTreeViewPrivate::AnimatedOperation::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate17AnimatedOperation3topEv(
    const QTreeViewPrivate::AnimatedOperation *self) {
  return self->top();
}

//  QRect QTreeViewPrivate::AnimatedOperation::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QTreeViewPrivate17AnimatedOperation4rectEv(
    const QTreeViewPrivate::AnimatedOperation *self) {
  return new QRect(self->rect());
}

//  void QTreeViewPrivate::AnimatedOperation::updateCurrentValue(const
//      QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate17AnimatedOperation18updateCurrentValueERK8QVariant(
    QTreeViewPrivate::AnimatedOperation *self,
    const QVariant *a0) {
  self->updateCurrentValue(*a0);
}

//  void QTreeViewPrivate::AnimatedOperation::updateState(State state, State
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate17AnimatedOperation11updateStateEN18QAbstractAnimation5StateES2_(
    QTreeViewPrivate::AnimatedOperation *self,
    QAbstractAnimation::State state,
    QAbstractAnimation::State a1) {
  self->updateState(state, a1);
}

//  a Python function taken by a CuteQTreeViewPrivate_AnimatedOperation, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeViewPrivate_AnimatedOperation(
    QTreeViewPrivate::AnimatedOperation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTreeViewPrivate_AnimatedOperation *>(self)->take(key, call);
}

//  void QTreeViewPrivate::AnimatedOperation::updateCurrentValue(const
//      QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTreeViewPrivate17AnimatedOperation18updateCurrentValueERK8QVariant(
    QTreeViewPrivate::AnimatedOperation *self,
    const QVariant *a0) {
  self->QTreeViewPrivate::AnimatedOperation::updateCurrentValue(*a0);
}

//  void QTreeViewPrivate::AnimatedOperation::updateState(State state, State
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTreeViewPrivate17AnimatedOperation11updateStateEN18QAbstractAnimation5StateES2_(
    QTreeViewPrivate::AnimatedOperation *self,
    QAbstractAnimation::State state,
    QAbstractAnimation::State a1) {
  self->QTreeViewPrivate::AnimatedOperation::updateState(state, a1);
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(treeview)

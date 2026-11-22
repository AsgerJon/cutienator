//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qbuttongroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qbuttongroup.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qabstractbutton.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QButtonGroup that Python can take functions over in. Every QButtonGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQButtonGroupCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQButtonGroupCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQButtonGroupCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQButtonGroupCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQButtonGroupCall4)(const void *, QEvent *, int *);
typedef void (*CuteQButtonGroupCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQButtonGroupCall6)(const void *, const QMetaMethod *, int *);
class CuteQButtonGroup : public QButtonGroup {
public:
  using QButtonGroup::QButtonGroup;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQButtonGroupCall0 call = reinterpret_cast<CuteQButtonGroupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQButtonGroupCall1 call = reinterpret_cast<CuteQButtonGroupCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQButtonGroupCall2 call = reinterpret_cast<CuteQButtonGroupCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQButtonGroupCall3 call = reinterpret_cast<CuteQButtonGroupCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQButtonGroupCall4 call = reinterpret_cast<CuteQButtonGroupCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQButtonGroupCall5 call = reinterpret_cast<CuteQButtonGroupCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQButtonGroupCall6 call = reinterpret_cast<CuteQButtonGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QButtonGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QButtonGroup10metaObjectEv(
    const QButtonGroup *self) {
  return self->metaObject();
}

//  QString QButtonGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QButtonGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QButtonGroup::tr(s, c, n));
}

//  QButtonGroup::QButtonGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QButtonGroup *ritual_ZN12QButtonGroupC1EP7QObject(QObject *parent) {
  return new CuteQButtonGroup(parent);
}

//  QButtonGroup::~QButtonGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroupD1Ev(QButtonGroup *self) {
  delete self;
}

//  void QButtonGroup::setExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup12setExclusiveEb(QButtonGroup *self, bool a0) {
  self->setExclusive(a0);
}

//  bool QButtonGroup::exclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QButtonGroup9exclusiveEv(const QButtonGroup *self) {
  return self->exclusive();
}

//  void QButtonGroup::addButton(QAbstractButton *a0, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup9addButtonEP15QAbstractButtoni(
    QButtonGroup *self,
    QAbstractButton *a0,
    int id) {
  self->addButton(a0, id);
}

//  void QButtonGroup::removeButton(QAbstractButton *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup12removeButtonEP15QAbstractButton(
    QButtonGroup *self,
    QAbstractButton *a0) {
  self->removeButton(a0);
}

//  QList<QAbstractButton *> QButtonGroup::buttons() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK12QButtonGroup7buttonsEv(
    const QButtonGroup *self) {
  return new QList<QAbstractButton *>(self->buttons());
}

//  QAbstractButton *QButtonGroup::checkedButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK12QButtonGroup13checkedButtonEv(
    const QButtonGroup *self) {
  return self->checkedButton();
}

//  QAbstractButton *QButtonGroup::button(int id) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK12QButtonGroup6buttonEi(
    const QButtonGroup *self,
    int id) {
  return self->button(id);
}

//  void QButtonGroup::setId(QAbstractButton *button, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup5setIdEP15QAbstractButtoni(
    QButtonGroup *self,
    QAbstractButton *button,
    int id) {
  self->setId(button, id);
}

//  int QButtonGroup::id(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QButtonGroup2idEP15QAbstractButton(
    const QButtonGroup *self,
    QAbstractButton *button) {
  return self->id(button);
}

//  int QButtonGroup::checkedId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QButtonGroup9checkedIdEv(const QButtonGroup *self) {
  return self->checkedId();
}

//  a Python function taken by a CuteQButtonGroup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QButtonGroup(
    QButtonGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQButtonGroup *>(self)->take(key, call);
}

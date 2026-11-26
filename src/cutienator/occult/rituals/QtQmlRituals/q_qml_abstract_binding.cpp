//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlabstractbinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlabstractbinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlAbstractBinding that Python can take functions over in. Every QQmlAbstractBinding
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQmlAbstractBindingCall0)(const void *, int *);
typedef int (*CuteQQmlAbstractBindingCall1)(const void *, int *);
typedef void (*CuteQQmlAbstractBindingCall2)(const void *, bool, int, int *);
typedef void (*CuteQQmlAbstractBindingCall3)(const void *, const QQmlProperty *, int *);
class CuteQQmlAbstractBinding : public QQmlAbstractBinding {
public:
  using QQmlAbstractBinding::QQmlAbstractBinding;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QQmlAbstractBinding10expressionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QQmlAbstractBinding4kindEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QString QQmlAbstractBinding::expression() const
  QString expression() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractBindingCall0 call = reinterpret_cast<CuteQQmlAbstractBindingCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlAbstractBinding::expression();
  }

  //  Kind QQmlAbstractBinding::kind() const
  QQmlAbstractBinding::Kind kind() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAbstractBindingCall1 call = reinterpret_cast<CuteQQmlAbstractBindingCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlAbstractBinding::Kind>(given);
    }
    return {};
  }

  //  void QQmlAbstractBinding::setEnabled(bool e,
  //      QQmlPropertyData::WriteFlags f)
  void setEnabled(bool e, QQmlPropertyData::WriteFlags f) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAbstractBindingCall2 call = reinterpret_cast<CuteQQmlAbstractBindingCall2>(taken[2]);
      call(this, e, static_cast<int>(f.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QQmlAbstractBinding::printBindingLoopError(const QQmlProperty
  //      &prop)
  void printBindingLoopError(const QQmlProperty &prop) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAbstractBindingCall3 call = reinterpret_cast<CuteQQmlAbstractBindingCall3>(taken[3]);
      call(this, &prop, &handled);
      if (handled) return;
    }
    QQmlAbstractBinding::printBindingLoopError(prop);
  }
};

//  QQmlAbstractBinding::QQmlAbstractBinding()
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZN19QQmlAbstractBindingC1Ev() {
  return new CuteQQmlAbstractBinding();
}

//  QQmlAbstractBinding::~QQmlAbstractBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBindingD1Ev(QQmlAbstractBinding *self) {
  delete self;
}

//  QString QQmlAbstractBinding::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlAbstractBinding10expressionEv(
    const QQmlAbstractBinding *self) {
  return new QString(self->expression());
}

//  Kind QQmlAbstractBinding::kind() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding::Kind ritual_ZNK19QQmlAbstractBinding4kindEv(
    const QQmlAbstractBinding *self) {
  return self->kind();
}

//  QQmlPropertyIndex QQmlAbstractBinding::targetPropertyIndex() const
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZNK19QQmlAbstractBinding19targetPropertyIndexEv(
    const QQmlAbstractBinding *self) {
  return new QQmlPropertyIndex(self->targetPropertyIndex());
}

//  QObject *QQmlAbstractBinding::targetObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK19QQmlAbstractBinding12targetObjectEv(
    const QQmlAbstractBinding *self) {
  return self->targetObject();
}

//  void QQmlAbstractBinding::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding9setTargetERK12QQmlProperty(
    QQmlAbstractBinding *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  bool QQmlAbstractBinding::setTarget(QObject *a0, const QQmlPropertyData
//      &a1, const QQmlPropertyData *valueType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlAbstractBinding9setTargetEP7QObjectRK16QQmlPropertyDataPS3_(
    QQmlAbstractBinding *self,
    QObject *a0,
    const QQmlPropertyData *a1,
    const QQmlPropertyData *valueType) {
  return self->setTarget(a0, *a1, valueType);
}

//  bool QQmlAbstractBinding::setTarget(QObject *a0, int coreIndex, bool
//      coreIsAlias, int valueTypeIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlAbstractBinding9setTargetEP7QObjectibi(
    QQmlAbstractBinding *self,
    QObject *a0,
    int coreIndex,
    bool coreIsAlias,
    int valueTypeIndex) {
  return self->setTarget(a0, coreIndex, coreIsAlias, valueTypeIndex);
}

//  void QQmlAbstractBinding::setEnabled(bool e, QQmlPropertyData::WriteFlags
//      f)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlAbstractBinding *self,
    bool e,
    int f) {
  self->setEnabled(e, QFlags<QQmlPropertyData::WriteFlag>::fromInt(f));
}

//  void QQmlAbstractBinding::addToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding11addToObjectEv(
    QQmlAbstractBinding *self) {
  self->addToObject();
}

//  void QQmlAbstractBinding::removeFromObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding16removeFromObjectEv(
    QQmlAbstractBinding *self) {
  self->removeFromObject();
}

//  void QQmlAbstractBinding::printBindingLoopError(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty(
    QQmlAbstractBinding *self,
    const QQmlProperty *prop) {
  self->printBindingLoopError(*prop);
}

//  QQmlAbstractBinding *QQmlAbstractBinding::nextBinding() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZNK19QQmlAbstractBinding11nextBindingEv(
    const QQmlAbstractBinding *self) {
  return self->nextBinding();
}

//  bool QQmlAbstractBinding::canUseAccessor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding14canUseAccessorEv(
    const QQmlAbstractBinding *self) {
  return self->canUseAccessor();
}

//  void QQmlAbstractBinding::setCanUseAccessor(bool canUseAccessor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding17setCanUseAccessorEb(
    QQmlAbstractBinding *self,
    bool canUseAccessor) {
  self->setCanUseAccessor(canUseAccessor);
}

//  bool QQmlAbstractBinding::isSticky() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding8isStickyEv(
    const QQmlAbstractBinding *self) {
  return self->isSticky();
}

//  void QQmlAbstractBinding::setSticky(bool isSticky)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding9setStickyEb(
    QQmlAbstractBinding *self,
    bool isSticky) {
  self->setSticky(isSticky);
}

//  void QQmlAbstractBinding::setAddedToObject(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding16setAddedToObjectEb(
    QQmlAbstractBinding *self,
    bool v) {
  self->setAddedToObject(v);
}

//  bool QQmlAbstractBinding::isAddedToObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding15isAddedToObjectEv(
    const QQmlAbstractBinding *self) {
  return self->isAddedToObject();
}

//  void QQmlAbstractBinding::setNextBinding(QQmlAbstractBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding14setNextBindingEPS_(
    QQmlAbstractBinding *self,
    QQmlAbstractBinding *a0) {
  self->setNextBinding(a0);
}

//  void QQmlAbstractBinding::getPropertyData(const QQmlPropertyData
//      **propertyData, QQmlPropertyData *valueTypeData) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlAbstractBinding15getPropertyDataEPPK16QQmlPropertyDataPS0_(
    const QQmlAbstractBinding *self,
    const QQmlPropertyData **propertyData,
    QQmlPropertyData *valueTypeData) {
  self->getPropertyData(propertyData, valueTypeData);
}

//  bool QQmlAbstractBinding::updatingFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding12updatingFlagEv(
    const QQmlAbstractBinding *self) {
  return self->updatingFlag();
}

//  void QQmlAbstractBinding::setUpdatingFlag(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding15setUpdatingFlagEb(
    QQmlAbstractBinding *self,
    bool a0) {
  self->setUpdatingFlag(a0);
}

//  bool QQmlAbstractBinding::enabledFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding11enabledFlagEv(
    const QQmlAbstractBinding *self) {
  return self->enabledFlag();
}

//  void QQmlAbstractBinding::setEnabledFlag(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding14setEnabledFlagEb(
    QQmlAbstractBinding *self,
    bool a0) {
  self->setEnabledFlag(a0);
}

//  void QQmlAbstractBinding::updateCanUseAccessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding20updateCanUseAccessorEv(
    QQmlAbstractBinding *self) {
  self->updateCanUseAccessor();
}

//  void QQmlAbstractBinding::setState(State state, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding8setStateENS_5StateEb(
    QQmlAbstractBinding *self,
    QQmlAbstractBinding::State state,
    bool enabled) {
  self->setState(state, enabled);
}

//  bool QQmlAbstractBinding::hasState(State state) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlAbstractBinding8hasStateENS_5StateE(
    const QQmlAbstractBinding *self,
    QQmlAbstractBinding::State state) {
  return self->hasState(state);
}

//  a Python function taken by a CuteQQmlAbstractBinding, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractBinding(
    QQmlAbstractBinding *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractBinding *>(self)->take(key, call);
}

//  QString QQmlAbstractBinding::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QQmlAbstractBinding10expressionEv(
    const QQmlAbstractBinding *self) {
  return new QString(self->QQmlAbstractBinding::expression());
}

//  void QQmlAbstractBinding::printBindingLoopError(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty(
    QQmlAbstractBinding *self,
    const QQmlProperty *prop) {
  self->QQmlAbstractBinding::printBindingLoopError(*prop);
}

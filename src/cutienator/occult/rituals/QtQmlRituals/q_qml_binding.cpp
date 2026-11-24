//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbinding_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlBinding that Python can take functions over in. Every QQmlBinding
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlBindingCall0)(const void *, int *);
typedef void (*CuteQQmlBindingCall1)(const void *, bool, int, int *);
typedef QString * (*CuteQQmlBindingCall2)(const void *, int *);
typedef void (*CuteQQmlBindingCall3)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQmlBindingCall4)(const void *, int *);
typedef const QQmlSourceLocation * (*CuteQQmlBindingCall5)(const void *, int *);
typedef bool (*CuteQQmlBindingCall6)(const void *, int *);
typedef bool (*CuteQQmlBindingCall7)(const void *, const QV4::Value *, bool, int, int *);
typedef QString * (*CuteQQmlBindingCall8)(const void *, int *);
class CuteQQmlBinding : public QQmlBinding {
public:
  using QQmlBinding::QQmlBinding;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQmlJavaScriptExpression7refreshEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QQmlAbstractBinding10expressionEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQmlJavaScriptExpression17expressionChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression14sourceLocationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QQmlBinding15hasDependenciesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQmlBinding5writeERKN3QV45ValueEb6QFlagsIN16QQmlPropertyData9WriteFlagEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QQmlBinding::refresh()
  void refresh() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlBindingCall0 call = reinterpret_cast<CuteQQmlBindingCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlBinding::refresh();
  }

  //  void QQmlBinding::setEnabled(bool a0, QQmlPropertyData::WriteFlags
  //      flags)
  void setEnabled(bool a0, QQmlPropertyData::WriteFlags flags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlBindingCall1 call = reinterpret_cast<CuteQQmlBindingCall1>(taken[1]);
      call(this, a0, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QQmlBinding::setEnabled(a0, flags);
  }

  //  QString QQmlBinding::expression() const
  QString expression() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlBindingCall2 call = reinterpret_cast<CuteQQmlBindingCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlBinding::expression();
  }

  //  void QQmlBinding::printBindingLoopError(const QQmlProperty &prop)
  void printBindingLoopError(const QQmlProperty &prop) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlBindingCall3 call = reinterpret_cast<CuteQQmlBindingCall3>(taken[3]);
      call(this, &prop, &handled);
      if (handled) return;
    }
    QQmlBinding::printBindingLoopError(prop);
  }

  //  void QQmlBinding::expressionChanged()
  void expressionChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlBindingCall4 call = reinterpret_cast<CuteQQmlBindingCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlBinding::expressionChanged();
  }

  //  QQmlSourceLocation QQmlBinding::sourceLocation() const
  QQmlSourceLocation sourceLocation() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlBindingCall5 call = reinterpret_cast<CuteQQmlBindingCall5>(taken[5]);
      const QQmlSourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlBinding::sourceLocation();
  }

  //  bool QQmlBinding::hasDependencies() const
  bool hasDependencies() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlBindingCall6 call = reinterpret_cast<CuteQQmlBindingCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlBinding::hasDependencies();
  }

  //  bool QQmlBinding::write(const QV4::Value &result, bool isUndefined,
  //      QQmlPropertyData::WriteFlags flags)
  bool write(
      const QV4::Value &result,
      bool isUndefined,
      QQmlPropertyData::WriteFlags flags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlBindingCall7 call = reinterpret_cast<CuteQQmlBindingCall7>(taken[7]);
      bool given = call(this, &result, isUndefined, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QQmlJavaScriptExpression::expressionIdentifier() const
  QString expressionIdentifier() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlBindingCall8 call = reinterpret_cast<CuteQQmlBindingCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlJavaScriptExpression::expressionIdentifier();
  }
};

//  QQmlBinding *QQmlBinding::create(const QQmlPropertyData *a0, const
//      QQmlScriptString &a1, QObject *a2, QQmlContext *a3)
extern "C" Q_DECL_EXPORT
QQmlBinding *ritual_ZN11QQmlBinding6createEPK16QQmlPropertyDataRK16QQmlScriptStringP7QObjectP11QQmlContext(
    const QQmlPropertyData *a0,
    const QQmlScriptString *a1,
    QObject *a2,
    QQmlContext *a3) {
  return QQmlBinding::create(a0, *a1, a2, a3);
}

//  Kind QQmlBinding::kind() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding::Kind ritual_ZNK11QQmlBinding4kindEv(
    const QQmlBinding *self) {
  return self->kind();
}

//  QQmlBinding::~QQmlBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBindingD1Ev(QQmlBinding *self) {
  delete self;
}

//  bool QQmlBinding::mustCaptureBindableProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlBinding27mustCaptureBindablePropertyEv(
    const QQmlBinding *self) {
  return self->mustCaptureBindableProperty();
}

//  void QQmlBinding::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding7refreshEv(QQmlBinding *self) {
  self->refresh();
}

//  void QQmlBinding::setEnabled(bool a0, QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlBinding *self,
    bool a0,
    int flags) {
  self->setEnabled(a0, QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  QString QQmlBinding::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlBinding10expressionEv(const QQmlBinding *self) {
  return new QString(self->expression());
}

//  void QQmlBinding::update(QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding6updateE6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlBinding *self,
    int flags) {
  self->update(QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  void QQmlBinding::printBindingLoopError(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding21printBindingLoopErrorERK12QQmlProperty(
    QQmlBinding *self,
    const QQmlProperty *prop) {
  self->printBindingLoopError(*prop);
}

//  QVariant QQmlBinding::evaluate()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN11QQmlBinding8evaluateEv(QQmlBinding *self) {
  return new QVariant(self->evaluate());
}

//  void QQmlBinding::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding17expressionChangedEv(QQmlBinding *self) {
  self->expressionChanged();
}

//  QQmlSourceLocation QQmlBinding::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZNK11QQmlBinding14sourceLocationEv(
    const QQmlBinding *self) {
  return new QQmlSourceLocation(self->sourceLocation());
}

//  void QQmlBinding::setSourceLocation(const QQmlSourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding17setSourceLocationERK18QQmlSourceLocation(
    QQmlBinding *self,
    const QQmlSourceLocation *location) {
  self->setSourceLocation(*location);
}

//  void QQmlBinding::setBoundFunction(QV4::BoundFunction *boundFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlBinding16setBoundFunctionEPN3QV413BoundFunctionE(
    QQmlBinding *self,
    QV4::BoundFunction *boundFunction) {
  self->setBoundFunction(boundFunction);
}

//  bool QQmlBinding::hasBoundFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlBinding16hasBoundFunctionEv(const QQmlBinding *self) {
  return self->hasBoundFunction();
}

//  QList<QQmlProperty> QQmlBinding::dependencies() const
extern "C" Q_DECL_EXPORT
QList<QQmlProperty> *ritual_ZNK11QQmlBinding12dependenciesEv(
    const QQmlBinding *self) {
  return new QList<QQmlProperty>(self->dependencies());
}

//  bool QQmlBinding::hasDependencies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlBinding15hasDependenciesEv(const QQmlBinding *self) {
  return self->hasDependencies();
}

//  bool QQmlBinding::write(const QV4::Value &result, bool isUndefined,
//      QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlBinding5writeERKN3QV45ValueEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlBinding *self,
    const QV4::Value *result,
    bool isUndefined,
    int flags) {
  return self->write(
      *result,
      isUndefined,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  bool QQmlBinding::slowWrite(const QQmlPropertyData &core, const
//      QQmlPropertyData &valueTypeData, const QV4::Value &result, bool
//      isUndefined, QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlBinding9slowWriteERK16QQmlPropertyDataS2_RKN3QV45ValueEb6QFlagsINS0_9WriteFlagEE(
    QQmlBinding *self,
    const QQmlPropertyData *core,
    const QQmlPropertyData *valueTypeData,
    const QV4::Value *result,
    bool isUndefined,
    int flags) {
  return self->slowWrite(
      *core,
      *valueTypeData,
      *result,
      isUndefined,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  QV4::ReturnedValue QQmlBinding::evaluate(bool *isUndefined)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN11QQmlBinding8evaluateEPb(
    QQmlBinding *self,
    bool *isUndefined) {
  return self->evaluate(isUndefined);
}

//  QQmlBinding *QQmlBinding::newBinding(const QQmlPropertyData *property)
extern "C" Q_DECL_EXPORT
QQmlBinding *ritual_ZN11QQmlBinding10newBindingEPK16QQmlPropertyData(
    const QQmlPropertyData *property) {
  return QQmlBinding::newBinding(property);
}

//  QQmlBinding *QQmlBinding::newBinding(QMetaType propertyType)
extern "C" Q_DECL_EXPORT
QQmlBinding *ritual_ZN11QQmlBinding10newBindingE9QMetaType(
    const QMetaType *propertyType) {
  return QQmlBinding::newBinding(*propertyType);
}

//  QQmlBinding as the QQmlAbstractBinding it is built on
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_cast_QQmlBinding_QQmlAbstractBinding(
    QQmlBinding *self) {
  return static_cast<QQmlAbstractBinding *>(self);
}

//  a Python function taken by a CuteQQmlBinding, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlBinding(
    QQmlBinding *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlBinding *>(self)->take(key, call);
}

//  void QQmlBinding::refresh()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQmlBinding7refreshEv(QQmlBinding *self) {
  self->QQmlBinding::refresh();
}

//  void QQmlBinding::setEnabled(bool a0, QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQmlBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlBinding *self,
    bool a0,
    int flags) {
  self->QQmlBinding::setEnabled(
      a0,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  QString QQmlBinding::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QQmlBinding10expressionEv(const QQmlBinding *self) {
  return new QString(self->QQmlBinding::expression());
}

//  void QQmlBinding::printBindingLoopError(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQmlBinding21printBindingLoopErrorERK12QQmlProperty(
    QQmlBinding *self,
    const QQmlProperty *prop) {
  self->QQmlBinding::printBindingLoopError(*prop);
}

//  void QQmlBinding::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQmlBinding17expressionChangedEv(QQmlBinding *self) {
  self->QQmlBinding::expressionChanged();
}

//  QQmlSourceLocation QQmlBinding::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_own_ZNK11QQmlBinding14sourceLocationEv(
    const QQmlBinding *self) {
  return new QQmlSourceLocation(self->QQmlBinding::sourceLocation());
}

//  bool QQmlBinding::hasDependencies() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QQmlBinding15hasDependenciesEv(
    const QQmlBinding *self) {
  return self->QQmlBinding::hasDependencies();
}

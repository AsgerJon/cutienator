//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugstatesdelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugstatesdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QQmlDebugStatesDelegate that Python can take functions over in. Every QQmlDebugStatesDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugStatesDelegateCall0)(const void *, QObject *, const QString *, const QVariant *, bool, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlDebugStatesDelegateCall1)(const void *, QObject *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
class CuteQQmlDebugStatesDelegate : public QQmlDebugStatesDelegate {
public:
  using QQmlDebugStatesDelegate::QQmlDebugStatesDelegate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN23QQmlDebugStatesDelegate28setBindingForInvalidPropertyEP7QObjectRK7QStringRK8QVariantb")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN23QQmlDebugStatesDelegate30resetBindingForInvalidPropertyEP7QObjectRK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
    return false;
  }

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugStatesDelegate::setBindingForInvalidProperty(QObject
  //      *object, const QString &propertyName, const QVariant &expression,
  //      bool isLiteralValue)
  bool setBindingForInvalidProperty(
      QObject *object,
      const QString &propertyName,
      const QVariant &expression,
      bool isLiteralValue) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugStatesDelegateCall0 call = reinterpret_cast<CuteQQmlDebugStatesDelegateCall0>(taken[0]);
      bool given = call(this, object, &propertyName, &expression, isLiteralValue, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlDebugStatesDelegate::resetBindingForInvalidProperty(QObject
  //      *object, const QString &propertyName)
  void resetBindingForInvalidProperty(
      QObject *object,
      const QString &propertyName) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugStatesDelegateCall1 call = reinterpret_cast<CuteQQmlDebugStatesDelegateCall1>(taken[1]);
      call(this, object, &propertyName, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))
};

//  QQmlDebugStatesDelegate::~QQmlDebugStatesDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlDebugStatesDelegateD1Ev(QQmlDebugStatesDelegate *self) {
  delete self;
}

//  void QQmlDebugStatesDelegate::updateBinding(QQmlContext *context, const
//      QQmlProperty &property, const QVariant &expression, bool
//      isLiteralValue, const QString &fileName, int line, int column, bool
//      *inBaseState)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlDebugStatesDelegate13updateBindingEP11QQmlContextRK12QQmlPropertyRK8QVariantbRK7QStringiiPb(
    QQmlDebugStatesDelegate *self,
    QQmlContext *context,
    const QQmlProperty *property,
    const QVariant *expression,
    bool isLiteralValue,
    const QString *fileName,
    int line,
    int column,
    bool *inBaseState) {
  self->updateBinding(
      context,
      *property,
      *expression,
      isLiteralValue,
      *fileName,
      line,
      column,
      inBaseState);
}

//  bool QQmlDebugStatesDelegate::setBindingForInvalidProperty(QObject
//      *object, const QString &propertyName, const QVariant &expression,
//      bool isLiteralValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQmlDebugStatesDelegate28setBindingForInvalidPropertyEP7QObjectRK7QStringRK8QVariantb(
    QQmlDebugStatesDelegate *self,
    QObject *object,
    const QString *propertyName,
    const QVariant *expression,
    bool isLiteralValue) {
  return self->setBindingForInvalidProperty(
      object,
      *propertyName,
      *expression,
      isLiteralValue);
}

//  void QQmlDebugStatesDelegate::resetBindingForInvalidProperty(QObject
//      *object, const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlDebugStatesDelegate30resetBindingForInvalidPropertyEP7QObjectRK7QString(
    QQmlDebugStatesDelegate *self,
    QObject *object,
    const QString *propertyName) {
  self->resetBindingForInvalidProperty(object, *propertyName);
}

//  a Python function taken by a CuteQQmlDebugStatesDelegate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugStatesDelegate(
    QQmlDebugStatesDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugStatesDelegate *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))

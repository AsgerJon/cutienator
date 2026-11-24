//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodelcolumn_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/qtlabsqmlmodelsexports.h>
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/QtLabsQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodelcolumn_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlTableModelColumn that Python can take functions over in. Every QQmlTableModelColumn
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableModelColumnCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableModelColumnCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelColumnCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelColumnCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelColumnCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelColumnCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelColumnCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlTableModelColumn : public QQmlTableModelColumn {
public:
  using QQmlTableModelColumn::QQmlTableModelColumn;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall0 call = reinterpret_cast<CuteQQmlTableModelColumnCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall1 call = reinterpret_cast<CuteQQmlTableModelColumnCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall2 call = reinterpret_cast<CuteQQmlTableModelColumnCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall3 call = reinterpret_cast<CuteQQmlTableModelColumnCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall4 call = reinterpret_cast<CuteQQmlTableModelColumnCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall5 call = reinterpret_cast<CuteQQmlTableModelColumnCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTableModelColumnCall6 call = reinterpret_cast<CuteQQmlTableModelColumnCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlTableModelColumn::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlTableModelColumn10metaObjectEv(
    const QQmlTableModelColumn *self) {
  return self->metaObject();
}

//  QString QQmlTableModelColumn::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlTableModelColumn2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTableModelColumn::tr(s, c, n));
}

//  QQmlTableModelColumn::QQmlTableModelColumn(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTableModelColumn *ritual_ZN20QQmlTableModelColumnC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlTableModelColumn(parent);
}

//  QQmlTableModelColumn::~QQmlTableModelColumn()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumnD1Ev(QQmlTableModelColumn *self) {
  delete self;
}

//  QJSValue QQmlTableModelColumn::display() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn7displayEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->display());
}

//  void QQmlTableModelColumn::setDisplay(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn10setDisplayERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setDisplay(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::decoration() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn10decorationEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->decoration());
}

//  void QQmlTableModelColumn::setDecoration(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn13setDecorationERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setDecoration(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::edit() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn4editEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->edit());
}

//  void QQmlTableModelColumn::setEdit(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn7setEditERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setEdit(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::toolTip() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn7toolTipEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->toolTip());
}

//  void QQmlTableModelColumn::setToolTip(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn10setToolTipERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setToolTip(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::statusTip() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn9statusTipEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->statusTip());
}

//  void QQmlTableModelColumn::setStatusTip(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn12setStatusTipERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setStatusTip(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::whatsThis() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn9whatsThisEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->whatsThis());
}

//  void QQmlTableModelColumn::setWhatsThis(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn12setWhatsThisERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setWhatsThis(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::font() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn4fontEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->font());
}

//  void QQmlTableModelColumn::setFont(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn7setFontERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setFont(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::textAlignment() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn13textAlignmentEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->textAlignment());
}

//  void QQmlTableModelColumn::setTextAlignment(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn16setTextAlignmentERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setTextAlignment(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::background() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn10backgroundEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->background());
}

//  void QQmlTableModelColumn::setBackground(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn13setBackgroundERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setBackground(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::foreground() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn10foregroundEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->foreground());
}

//  void QQmlTableModelColumn::setForeground(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn13setForegroundERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setForeground(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::checkState() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn10checkStateEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->checkState());
}

//  void QQmlTableModelColumn::setCheckState(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn13setCheckStateERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setCheckState(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::accessibleText() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn14accessibleTextEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->accessibleText());
}

//  void QQmlTableModelColumn::setAccessibleText(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn17setAccessibleTextERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setAccessibleText(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::accessibleDescription() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn21accessibleDescriptionEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->accessibleDescription());
}

//  void QQmlTableModelColumn::setAccessibleDescription(const QJSValue
//      &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn24setAccessibleDescriptionERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setAccessibleDescription(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::sizeHint() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK20QQmlTableModelColumn8sizeHintEv(
    const QQmlTableModelColumn *self) {
  return new QJSValue(self->sizeHint());
}

//  void QQmlTableModelColumn::setSizeHint(const QJSValue &stringOrFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTableModelColumn11setSizeHintERK8QJSValue(
    QQmlTableModelColumn *self,
    const QJSValue *stringOrFunction) {
  self->setSizeHint(*stringOrFunction);
}

//  QJSValue QQmlTableModelColumn::getterAtRole(const QString &roleName)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN20QQmlTableModelColumn12getterAtRoleERK7QString(
    QQmlTableModelColumn *self,
    const QString *roleName) {
  return new QJSValue(self->getterAtRole(*roleName));
}

//  const QHash<QString, QJSValue> QQmlTableModelColumn::getters() const
extern "C" Q_DECL_EXPORT
QHash<QString, QJSValue> *ritual_ZNK20QQmlTableModelColumn7gettersEv(
    const QQmlTableModelColumn *self) {
  return new QHash<QString, QJSValue>(self->getters());
}

//  a Python function taken by a CuteQQmlTableModelColumn, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTableModelColumn(
    QQmlTableModelColumn *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTableModelColumn *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_table_model)

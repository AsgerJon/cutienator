//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlexpression.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlexpression.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlscriptstring.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlExpression that Python can take functions over in. Every QQmlExpression
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlExpressionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlExpressionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExpressionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExpressionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExpressionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExpressionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExpressionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlExpression : public QQmlExpression {
public:
  using QQmlExpression::QQmlExpression;
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
      CuteQQmlExpressionCall0 call = reinterpret_cast<CuteQQmlExpressionCall0>(taken[0]);
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
      CuteQQmlExpressionCall1 call = reinterpret_cast<CuteQQmlExpressionCall1>(taken[1]);
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
      CuteQQmlExpressionCall2 call = reinterpret_cast<CuteQQmlExpressionCall2>(taken[2]);
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
      CuteQQmlExpressionCall3 call = reinterpret_cast<CuteQQmlExpressionCall3>(taken[3]);
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
      CuteQQmlExpressionCall4 call = reinterpret_cast<CuteQQmlExpressionCall4>(taken[4]);
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
      CuteQQmlExpressionCall5 call = reinterpret_cast<CuteQQmlExpressionCall5>(taken[5]);
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
      CuteQQmlExpressionCall6 call = reinterpret_cast<CuteQQmlExpressionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlExpression::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlExpression10metaObjectEv(
    const QQmlExpression *self) {
  return self->metaObject();
}

//  QString QQmlExpression::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlExpression2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlExpression::tr(s, c, n));
}

//  QQmlExpression::QQmlExpression()
extern "C" Q_DECL_EXPORT
QQmlExpression *ritual_ZN14QQmlExpressionC1Ev() {
  return new CuteQQmlExpression();
}

//  QQmlExpression::QQmlExpression(QQmlContext *a0, QObject *a1, const
//      QString &a2, QObject *a3)
extern "C" Q_DECL_EXPORT
QQmlExpression *ritual_ZN14QQmlExpressionC1EP11QQmlContextP7QObjectRK7QStringS3_(
    QQmlContext *a0,
    QObject *a1,
    const QString *a2,
    QObject *a3) {
  return new CuteQQmlExpression(a0, a1, *a2, a3);
}

//  QQmlExpression::QQmlExpression(const QQmlScriptString &a0, QQmlContext
//      *a1, QObject *a2, QObject *a3)
extern "C" Q_DECL_EXPORT
QQmlExpression *ritual_ZN14QQmlExpressionC1ERK16QQmlScriptStringP11QQmlContextP7QObjectS6_(
    const QQmlScriptString *a0,
    QQmlContext *a1,
    QObject *a2,
    QObject *a3) {
  return new CuteQQmlExpression(*a0, a1, a2, a3);
}

//  QQmlExpression::~QQmlExpression()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlExpressionD1Ev(QQmlExpression *self) {
  delete self;
}

//  QQmlEngine *QQmlExpression::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK14QQmlExpression6engineEv(const QQmlExpression *self) {
  return self->engine();
}

//  QQmlContext *QQmlExpression::context() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK14QQmlExpression7contextEv(
    const QQmlExpression *self) {
  return self->context();
}

//  QString QQmlExpression::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlExpression10expressionEv(
    const QQmlExpression *self) {
  return new QString(self->expression());
}

//  void QQmlExpression::setExpression(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlExpression13setExpressionERK7QString(
    QQmlExpression *self,
    const QString *a0) {
  self->setExpression(*a0);
}

//  bool QQmlExpression::notifyOnValueChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlExpression20notifyOnValueChangedEv(
    const QQmlExpression *self) {
  return self->notifyOnValueChanged();
}

//  void QQmlExpression::setNotifyOnValueChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlExpression23setNotifyOnValueChangedEb(
    QQmlExpression *self,
    bool a0) {
  self->setNotifyOnValueChanged(a0);
}

//  QString QQmlExpression::sourceFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlExpression10sourceFileEv(
    const QQmlExpression *self) {
  return new QString(self->sourceFile());
}

//  int QQmlExpression::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlExpression10lineNumberEv(const QQmlExpression *self) {
  return self->lineNumber();
}

//  int QQmlExpression::columnNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlExpression12columnNumberEv(const QQmlExpression *self) {
  return self->columnNumber();
}

//  void QQmlExpression::setSourceLocation(const QString &fileName, int line,
//      int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlExpression17setSourceLocationERK7QStringii(
    QQmlExpression *self,
    const QString *fileName,
    int line,
    int column) {
  self->setSourceLocation(*fileName, line, column);
}

//  QObject *QQmlExpression::scopeObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK14QQmlExpression11scopeObjectEv(
    const QQmlExpression *self) {
  return self->scopeObject();
}

//  bool QQmlExpression::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlExpression8hasErrorEv(const QQmlExpression *self) {
  return self->hasError();
}

//  void QQmlExpression::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlExpression10clearErrorEv(QQmlExpression *self) {
  self->clearError();
}

//  QQmlError QQmlExpression::error() const
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZNK14QQmlExpression5errorEv(const QQmlExpression *self) {
  return new QQmlError(self->error());
}

//  QVariant QQmlExpression::evaluate(bool *valueIsUndefined)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QQmlExpression8evaluateEPb(
    QQmlExpression *self,
    bool *valueIsUndefined) {
  return new QVariant(self->evaluate(valueIsUndefined));
}

//  QQmlExpressionPrivate *QQmlExpression::d_func()
extern "C" Q_DECL_EXPORT
QQmlExpressionPrivate *ritual_ZN14QQmlExpression6d_funcEv(
    QQmlExpression *self) {
  return self->d_func();
}

//  const QQmlExpressionPrivate *QQmlExpression::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlExpressionPrivate *ritual_ZNK14QQmlExpression6d_funcEv(
    const QQmlExpression *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlExpression, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlExpression(
    QQmlExpression *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlExpression *>(self)->take(key, call);
}

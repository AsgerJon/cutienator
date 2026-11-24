//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmldatamodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmldatamodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QScxmlDataModel that Python can take functions over in. Every QScxmlDataModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScxmlDataModelCall0)(const void *, const QScxmlEvent *, int *);
typedef const QVariant * (*CuteQScxmlDataModelCall1)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlDataModelCall2)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlDataModelCall3)(const void *, const QString *, const QVariant *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDataModelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDataModelCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlDataModel : public QScxmlDataModel {
public:
  using QScxmlDataModel::QScxmlDataModel;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QScxmlDataModel13setScxmlEventERK11QScxmlEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel13scxmlPropertyERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QScxmlDataModel::setScxmlEvent(const QScxmlEvent &event)
  void setScxmlEvent(const QScxmlEvent &event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlDataModelCall0 call = reinterpret_cast<CuteQScxmlDataModelCall0>(taken[0]);
      call(this, &event, &handled);
      if (handled) return;
    }
  }

  //  QVariant QScxmlDataModel::scxmlProperty(const QString &name) const
  QVariant scxmlProperty(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlDataModelCall1 call = reinterpret_cast<CuteQScxmlDataModelCall1>(taken[1]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QScxmlDataModel::hasScxmlProperty(const QString &name) const
  bool hasScxmlProperty(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlDataModelCall2 call = reinterpret_cast<CuteQScxmlDataModelCall2>(taken[2]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QScxmlDataModel::setScxmlProperty(const QString &name, const
  //      QVariant &value, const QString &context)
  bool setScxmlProperty(
      const QString &name,
      const QVariant &value,
      const QString &context) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlDataModelCall3 call = reinterpret_cast<CuteQScxmlDataModelCall3>(taken[3]);
      bool given = call(this, &name, &value, &context, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlDataModelCall4 call = reinterpret_cast<CuteQScxmlDataModelCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScxmlDataModelCall5 call = reinterpret_cast<CuteQScxmlDataModelCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScxmlDataModelCall6 call = reinterpret_cast<CuteQScxmlDataModelCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScxmlDataModelCall7 call = reinterpret_cast<CuteQScxmlDataModelCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScxmlDataModelCall8 call = reinterpret_cast<CuteQScxmlDataModelCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScxmlDataModelCall9 call = reinterpret_cast<CuteQScxmlDataModelCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScxmlDataModelCall10 call = reinterpret_cast<CuteQScxmlDataModelCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlDataModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QScxmlDataModel10metaObjectEv(
    const QScxmlDataModel *self) {
  return self->metaObject();
}

//  QString QScxmlDataModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QScxmlDataModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlDataModel::tr(s, c, n));
}

//  QScxmlDataModelPrivate *QScxmlDataModel::d_func()
extern "C" Q_DECL_EXPORT
QScxmlDataModelPrivate *ritual_ZN15QScxmlDataModel6d_funcEv(
    QScxmlDataModel *self) {
  return self->d_func();
}

//  const QScxmlDataModelPrivate *QScxmlDataModel::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlDataModelPrivate *ritual_ZNK15QScxmlDataModel6d_funcEv(
    const QScxmlDataModel *self) {
  return self->d_func();
}

//  QScxmlDataModel *QScxmlDataModel::createScxmlDataModel(const QString
//      &pluginKey)
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZN15QScxmlDataModel20createScxmlDataModelERK7QString(
    const QString *pluginKey) {
  return QScxmlDataModel::createScxmlDataModel(*pluginKey);
}

//  void QScxmlDataModel::setStateMachine(QScxmlStateMachine *stateMachine)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel15setStateMachineEP18QScxmlStateMachine(
    QScxmlDataModel *self,
    QScxmlStateMachine *stateMachine) {
  self->setStateMachine(stateMachine);
}

//  QScxmlStateMachine *QScxmlDataModel::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK15QScxmlDataModel12stateMachineEv(
    const QScxmlDataModel *self) {
  return self->stateMachine();
}

//  bool QScxmlDataModel::setup(const QVariantMap &initialDataValues)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QScxmlDataModel5setupERK4QMapI7QString8QVariantE(
    QScxmlDataModel *self,
    const QMap<QString, QVariant> *initialDataValues) {
  return self->setup(*initialDataValues);
}

//  QString
//      QScxmlDataModel::evaluateToString(QScxmlExecutableContent::EvaluatorI
//      d id, bool *ok)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QScxmlDataModel16evaluateToStringEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return new QString(self->evaluateToString(id, ok));
}

//  bool QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId
//      id, bool *ok)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QScxmlDataModel14evaluateToBoolEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return self->evaluateToBool(id, ok);
}

//  QVariant
//      QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::Evaluator
//      Id id, bool *ok)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QScxmlDataModel17evaluateToVariantEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return new QVariant(self->evaluateToVariant(id, ok));
}

//  void QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId
//      id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel14evaluateToVoidEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateToVoid(id, ok);
}

//  void
//      QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::Evaluato
//      rId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel18evaluateAssignmentEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateAssignment(id, ok);
}

//  void QScxmlDataModel::evaluateInitialization(QScxmlExecutableContent::Eva
//      luatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel22evaluateInitializationEiPb(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateInitialization(id, ok);
}

//  void
//      QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId
//      id, bool *ok, ForeachLoopBody *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel15evaluateForeachEiPbPNS_15ForeachLoopBodyE(
    QScxmlDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok,
    QScxmlDataModel::ForeachLoopBody *body) {
  self->evaluateForeach(id, ok, body);
}

//  void QScxmlDataModel::setScxmlEvent(const QScxmlEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel13setScxmlEventERK11QScxmlEvent(
    QScxmlDataModel *self,
    const QScxmlEvent *event) {
  self->setScxmlEvent(*event);
}

//  QVariant QScxmlDataModel::scxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QScxmlDataModel13scxmlPropertyERK7QString(
    const QScxmlDataModel *self,
    const QString *name) {
  return new QVariant(self->scxmlProperty(*name));
}

//  bool QScxmlDataModel::hasScxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString(
    const QScxmlDataModel *self,
    const QString *name) {
  return self->hasScxmlProperty(*name);
}

//  bool QScxmlDataModel::setScxmlProperty(const QString &name, const
//      QVariant &value, const QString &context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_(
    QScxmlDataModel *self,
    const QString *name,
    const QVariant *value,
    const QString *context) {
  return self->setScxmlProperty(*name, *value, *context);
}

//  a Python function taken by a CuteQScxmlDataModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlDataModel(
    QScxmlDataModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlDataModel *>(self)->take(key, call);
}

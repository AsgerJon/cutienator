//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlcppdatamodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlcppdatamodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QScxmlCppDataModel that Python can take functions over in. Every QScxmlCppDataModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQScxmlCppDataModelCall0)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlCppDataModelCall1)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlCppDataModelCall2)(const void *, const QString *, const QVariant *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlCppDataModelCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlCppDataModelCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlCppDataModelCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlCppDataModelCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlCppDataModelCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlCppDataModelCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlCppDataModelCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlCppDataModel : public QScxmlCppDataModel {
public:
  using QScxmlCppDataModel::QScxmlCppDataModel;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel13scxmlPropertyERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QScxmlCppDataModel::scxmlProperty(const QString &name) const
  QVariant scxmlProperty(const QString &name) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall0 call = reinterpret_cast<CuteQScxmlCppDataModelCall0>(taken[0]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QScxmlCppDataModel::scxmlProperty(name);
  }

  //  bool QScxmlCppDataModel::hasScxmlProperty(const QString &name) const
  bool hasScxmlProperty(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall1 call = reinterpret_cast<CuteQScxmlCppDataModelCall1>(taken[1]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QScxmlCppDataModel::hasScxmlProperty(name);
  }

  //  bool QScxmlCppDataModel::setScxmlProperty(const QString &name, const
  //      QVariant &value, const QString &context)
  bool setScxmlProperty(
      const QString &name,
      const QVariant &value,
      const QString &context) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall2 call = reinterpret_cast<CuteQScxmlCppDataModelCall2>(taken[2]);
      bool given = call(this, &name, &value, &context, &handled);
      if (handled) return given;
    }
    return QScxmlCppDataModel::setScxmlProperty(name, value, context);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall3 call = reinterpret_cast<CuteQScxmlCppDataModelCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall4 call = reinterpret_cast<CuteQScxmlCppDataModelCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall5 call = reinterpret_cast<CuteQScxmlCppDataModelCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall6 call = reinterpret_cast<CuteQScxmlCppDataModelCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall7 call = reinterpret_cast<CuteQScxmlCppDataModelCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall8 call = reinterpret_cast<CuteQScxmlCppDataModelCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScxmlCppDataModelCall9 call = reinterpret_cast<CuteQScxmlCppDataModelCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlCppDataModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QScxmlCppDataModel10metaObjectEv(
    const QScxmlCppDataModel *self) {
  return self->metaObject();
}

//  void *QScxmlCppDataModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QScxmlCppDataModel11qt_metacastEPKc(
    QScxmlCppDataModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlCppDataModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QScxmlCppDataModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlCppDataModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlCppDataModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QScxmlCppDataModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlCppDataModel::tr(s, c, n));
}

//  QScxmlCppDataModelPrivate *QScxmlCppDataModel::d_func()
extern "C" Q_DECL_EXPORT
QScxmlCppDataModelPrivate *ritual_ZN18QScxmlCppDataModel6d_funcEv(
    QScxmlCppDataModel *self) {
  return self->d_func();
}

//  const QScxmlCppDataModelPrivate *QScxmlCppDataModel::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlCppDataModelPrivate *ritual_ZNK18QScxmlCppDataModel6d_funcEv(
    const QScxmlCppDataModel *self) {
  return self->d_func();
}

//  bool QScxmlCppDataModel::setup(const QVariantMap &initialDataValues)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QScxmlCppDataModel5setupERK4QMapI7QString8QVariantE(
    QScxmlCppDataModel *self,
    const QMap<QString, QVariant> *initialDataValues) {
  return self->setup(*initialDataValues);
}

//  void QScxmlCppDataModel::evaluateAssignment(QScxmlExecutableContent::Eval
//      uatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlCppDataModel18evaluateAssignmentEiPb(
    QScxmlCppDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateAssignment(id, ok);
}

//  void QScxmlCppDataModel::evaluateInitialization(QScxmlExecutableContent::
//      EvaluatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlCppDataModel22evaluateInitializationEiPb(
    QScxmlCppDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateInitialization(id, ok);
}

//  void
//      QScxmlCppDataModel::evaluateForeach(QScxmlExecutableContent::Evaluato
//      rId id, bool *ok, ForeachLoopBody *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlCppDataModel15evaluateForeachEiPbPN15QScxmlDataModel15ForeachLoopBodyE(
    QScxmlCppDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok,
    QScxmlDataModel::ForeachLoopBody *body) {
  self->evaluateForeach(id, ok, body);
}

//  void QScxmlCppDataModel::setScxmlEvent(const QScxmlEvent &scxmlEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlCppDataModel13setScxmlEventERK11QScxmlEvent(
    QScxmlCppDataModel *self,
    const QScxmlEvent *scxmlEvent) {
  self->setScxmlEvent(*scxmlEvent);
}

//  const QScxmlEvent &QScxmlCppDataModel::scxmlEvent() const
extern "C" Q_DECL_EXPORT
QScxmlEvent *ritual_ZNK18QScxmlCppDataModel10scxmlEventEv(
    const QScxmlCppDataModel *self) {
  return new QScxmlEvent(self->scxmlEvent());
}

//  QVariant QScxmlCppDataModel::scxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QScxmlCppDataModel13scxmlPropertyERK7QString(
    const QScxmlCppDataModel *self,
    const QString *name) {
  return new QVariant(self->scxmlProperty(*name));
}

//  bool QScxmlCppDataModel::hasScxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlCppDataModel16hasScxmlPropertyERK7QString(
    const QScxmlCppDataModel *self,
    const QString *name) {
  return self->hasScxmlProperty(*name);
}

//  bool QScxmlCppDataModel::setScxmlProperty(const QString &name, const
//      QVariant &value, const QString &context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QScxmlCppDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_(
    QScxmlCppDataModel *self,
    const QString *name,
    const QVariant *value,
    const QString *context) {
  return self->setScxmlProperty(*name, *value, *context);
}

//  bool QScxmlCppDataModel::inState(const QString &stateName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlCppDataModel7inStateERK7QString(
    const QScxmlCppDataModel *self,
    const QString *stateName) {
  return self->inState(*stateName);
}

//  a Python function taken by a CuteQScxmlCppDataModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlCppDataModel(
    QScxmlCppDataModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlCppDataModel *>(self)->take(key, call);
}

//  QVariant QScxmlCppDataModel::scxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QScxmlCppDataModel13scxmlPropertyERK7QString(
    const QScxmlCppDataModel *self,
    const QString *name) {
  return new QVariant(self->QScxmlCppDataModel::scxmlProperty(*name));
}

//  bool QScxmlCppDataModel::hasScxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QScxmlCppDataModel16hasScxmlPropertyERK7QString(
    const QScxmlCppDataModel *self,
    const QString *name) {
  return self->QScxmlCppDataModel::hasScxmlProperty(*name);
}

//  bool QScxmlCppDataModel::setScxmlProperty(const QString &name, const
//      QVariant &value, const QString &context)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QScxmlCppDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_(
    QScxmlCppDataModel *self,
    const QString *name,
    const QVariant *value,
    const QString *context) {
  return self->QScxmlCppDataModel::setScxmlProperty(*name, *value, *context);
}

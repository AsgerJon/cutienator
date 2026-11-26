//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverrouterrule.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtHttpServer/qhttpserverrouterrule.h>
#include <QtCore/qstring.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <cstring>
#include <QtCore/QMetaType>

//  Only a class built on QHttpServerRouterRule may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQHttpServerRouterRule : QHttpServerRouterRule {
  using QHttpServerRouterRule::matches;
};

//  A QHttpServerRouterRule that Python can take functions over in. Every QHttpServerRouterRule
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQHttpServerRouterRuleCall0)(const void *, const QHttpServerRequest *, QRegularExpressionMatch *, int *);
class CuteQHttpServerRouterRule : public QHttpServerRouterRule {
public:
  using QHttpServerRouterRule::QHttpServerRouterRule;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerRequestP23QRegularExpressionMatch")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QHttpServerRouterRule::matches(const QHttpServerRequest
  //      &request, QRegularExpressionMatch *match) const
  bool matches(
      const QHttpServerRequest &request,
      QRegularExpressionMatch *match) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpServerRouterRuleCall0 call = reinterpret_cast<CuteQHttpServerRouterRuleCall0>(taken[0]);
      bool given = call(this, &request, match, &handled);
      if (handled) return given;
    }
    return QHttpServerRouterRule::matches(request, match);
  }
};

//  QHttpServerRouterRulePrivate *QHttpServerRouterRule::d_func()
extern "C" Q_DECL_EXPORT
QHttpServerRouterRulePrivate *ritual_ZN21QHttpServerRouterRule6d_funcEv(
    QHttpServerRouterRule *self) {
  return self->d_func();
}

//  const QHttpServerRouterRulePrivate *QHttpServerRouterRule::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpServerRouterRulePrivate *ritual_ZNK21QHttpServerRouterRule6d_funcEv(
    const QHttpServerRouterRule *self) {
  return self->d_func();
}

//  QHttpServerRouterRule::QHttpServerRouterRule(const QString &pathPattern,
//      const QHttpServerRequest::Methods methods, const QObject *context,
//      QtPrivate::QSlotObjectBase *slotObjRaw)
extern "C" Q_DECL_EXPORT
QHttpServerRouterRule *ritual_ZN21QHttpServerRouterRuleC1ERK7QString6QFlagsIN18QHttpServerRequest6MethodEEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    const QString *pathPattern,
    int methods,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slotObjRaw) {
  return new CuteQHttpServerRouterRule(
      *pathPattern,
      QFlags<QHttpServerRequest::Method>::fromInt(methods),
      context,
      slotObjRaw);
}

//  const QObject *QHttpServerRouterRule::contextObject() const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK21QHttpServerRouterRule13contextObjectEv(
    const QHttpServerRouterRule *self) {
  return self->contextObject();
}

//  QHttpServerRouterRule::~QHttpServerRouterRule()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttpServerRouterRuleD1Ev(QHttpServerRouterRule *self) {
  delete self;
}

//  bool QHttpServerRouterRule::exec(const QHttpServerRequest &request,
//      QHttpServerResponder &responder) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHttpServerRouterRule4execERK18QHttpServerRequestR20QHttpServerResponder(
    const QHttpServerRouterRule *self,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  return self->exec(*request, *responder);
}

//  bool QHttpServerRouterRule::hasValidMethods() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHttpServerRouterRule15hasValidMethodsEv(
    const QHttpServerRouterRule *self) {
  return self->hasValidMethods();
}

//  bool
//      QHttpServerRouterRule::createPathRegexp(std::initializer_list<QMetaTy
//      pe> metaTypes, const QHash<QMetaType, QString> &converters)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttpServerRouterRule16createPathRegexpESt16initializer_listI9QMetaTypeERK5QHashIS1_7QStringE(
    QHttpServerRouterRule *self,
    const std::initializer_list<QMetaType> *metaTypes,
    const QHash<QMetaType, QString> *converters) {
  return self->createPathRegexp(*metaTypes, *converters);
}

//  bool QHttpServerRouterRule::matches(const QHttpServerRequest &request,
//      QRegularExpressionMatch *match) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerRequestP23QRegularExpressionMatch(
    const QHttpServerRouterRule *self,
    const QHttpServerRequest *request,
    QRegularExpressionMatch *match) {
  return self->matches(*request, match);
}

//  QHttpServerRouterRule::QHttpServerRouterRule(QHttpServerRouterRulePrivate
//      *d)
extern "C" Q_DECL_EXPORT
QHttpServerRouterRule *ritual_ZN21QHttpServerRouterRuleC1EP28QHttpServerRouterRulePrivate(
    QHttpServerRouterRulePrivate *d) {
  return new CuteQHttpServerRouterRule(d);
}

//  a Python function taken by a CuteQHttpServerRouterRule, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpServerRouterRule(
    QHttpServerRouterRule *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpServerRouterRule *>(self)->take(key, call);
}

//  bool QHttpServerRouterRule::matches(const QHttpServerRequest &request,
//      QRegularExpressionMatch *match) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerRequestP23QRegularExpressionMatch(
    const QHttpServerRouterRule *self,
    const QHttpServerRequest *request,
    QRegularExpressionMatch *match) {
  return static_cast<const OwnQHttpServerRouterRule *>(self)->OwnQHttpServerRouterRule::matches(
      *request,
      match);
}

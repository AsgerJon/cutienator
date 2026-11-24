//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qproperty.h>

//  QQmlAnyBinding::QQmlAnyBinding()
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBindingC1Ev() {
  return new QQmlAnyBinding();
}

//  QQmlAnyBinding QQmlAnyBinding::ofProperty(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBinding10ofPropertyERK12QQmlProperty(
    const QQmlProperty *prop) {
  return new QQmlAnyBinding(QQmlAnyBinding::ofProperty(*prop));
}

//  QQmlAnyBinding QQmlAnyBinding::ofProperty(QObject *object,
//      QQmlPropertyIndex index)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBinding10ofPropertyEP7QObject17QQmlPropertyIndex(
    QObject *object,
    const QQmlPropertyIndex *index) {
  return new QQmlAnyBinding(QQmlAnyBinding::ofProperty(object, *index));
}

//  QQmlAnyBinding QQmlAnyBinding::takeFrom(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBinding8takeFromERK12QQmlProperty(
    const QQmlProperty *prop) {
  return new QQmlAnyBinding(QQmlAnyBinding::takeFrom(*prop));
}

//  QQmlAnyBinding QQmlAnyBinding::createFromScriptString(const QQmlProperty
//      &prop, const QQmlScriptString &script, QObject *obj, QQmlContext
//      *ctxt)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBinding22createFromScriptStringERK12QQmlPropertyRK16QQmlScriptStringP7QObjectP11QQmlContext(
    const QQmlProperty *prop,
    const QQmlScriptString *script,
    QObject *obj,
    QQmlContext *ctxt) {
  return new QQmlAnyBinding(
      QQmlAnyBinding::createFromScriptString(
          *prop,
          *script,
          obj,
          ctxt));
}

//  void QQmlAnyBinding::removeBindingFrom(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBinding17removeBindingFromERK12QQmlProperty(
    const QQmlProperty *prop) {
  QQmlAnyBinding::removeBindingFrom(*prop);
}

//  void QQmlAnyBinding::installOn(const QQmlProperty &target,
//      InterceptorMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBinding9installOnERK12QQmlPropertyNS_15InterceptorModeE(
    QQmlAnyBinding *self,
    const QQmlProperty *target,
    QQmlAnyBinding::InterceptorMode mode) {
  self->installOn(*target, mode);
}

//  bool QQmlAnyBinding::hasError()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlAnyBinding8hasErrorEv(QQmlAnyBinding *self) {
  return self->hasError();
}

//  bool QQmlAnyBinding::isSticky() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlAnyBinding8isStickyEv(const QQmlAnyBinding *self) {
  return self->isSticky();
}

//  void QQmlAnyBinding::setSticky(bool sticky)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBinding9setStickyEb(
    QQmlAnyBinding *self,
    bool sticky) {
  self->setSticky(sticky);
}

//  bool QQmlAnyBinding::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlAnyBindingcvbEv(const QQmlAnyBinding *self) {
  return self->operator bool();
}

//  bool QQmlAnyBinding::isAbstractPropertyBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlAnyBinding25isAbstractPropertyBindingEv(
    const QQmlAnyBinding *self) {
  return self->isAbstractPropertyBinding();
}

//  bool QQmlAnyBinding::isUntypedPropertyBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlAnyBinding24isUntypedPropertyBindingEv(
    const QQmlAnyBinding *self) {
  return self->isUntypedPropertyBinding();
}

//  QUntypedPropertyBinding QQmlAnyBinding::asUntypedPropertyBinding() const
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZNK14QQmlAnyBinding24asUntypedPropertyBindingEv(
    const QQmlAnyBinding *self) {
  return new QUntypedPropertyBinding(self->asUntypedPropertyBinding());
}

//  QQmlAbstractBinding *QQmlAnyBinding::asAbstractBinding() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZNK14QQmlAnyBinding17asAbstractBindingEv(
    const QQmlAnyBinding *self) {
  return self->asAbstractBinding();
}

//  void QQmlAnyBinding::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBinding7refreshEv(QQmlAnyBinding *self) {
  self->refresh();
}

//  QQmlAnyBinding::QQmlAnyBinding(const QQmlAnyBinding &other)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN14QQmlAnyBindingC1ERKS_(
    const QQmlAnyBinding *other) {
  return new QQmlAnyBinding(*other);
}

//  bool operator==(const QQmlAnyBinding &p1, const QQmlAnyBinding &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QQmlAnyBindingS1_(
    const QQmlAnyBinding *p1,
    const QQmlAnyBinding *p2) {
  return operator==(*p1, *p2);
}

//  bool operator!=(const QQmlAnyBinding &p1, const QQmlAnyBinding &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QQmlAnyBindingS1_(
    const QQmlAnyBinding *p1,
    const QQmlAnyBinding *p2) {
  return operator!=(*p1, *p2);
}

//  QQmlAnyBinding::~QQmlAnyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBindingD1Ev(QQmlAnyBinding *self) {
  delete self;
}

//  void QQmlAnyBinding::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlAnyBinding5clearEv(QQmlAnyBinding *self) {
  self->clear();
}

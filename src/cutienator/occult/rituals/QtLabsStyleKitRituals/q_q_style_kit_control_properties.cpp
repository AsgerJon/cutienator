//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <functional>
#include <QtCore/QString>

//  const QMetaObject *QQStyleKitControlProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQStyleKitControlProperties10metaObjectEv(
    const QQStyleKitControlProperties *self) {
  return self->metaObject();
}

//  void *QQStyleKitControlProperties::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQStyleKitControlProperties11qt_metacastEPKc(
    QQStyleKitControlProperties *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitControlProperties::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQStyleKitControlProperties11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitControlProperties *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitControlProperties::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQStyleKitControlProperties2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitControlProperties::tr(s, c, n));
}

//  void QQStyleKitControlProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitControlProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitControlProperties::QQStyleKitControlProperties(QQSK::PropertyGr
//      oup group, QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitControlProperties *ritual_ZN27QQStyleKitControlPropertiesC1EN4QQSK13PropertyGroupEP7QObject(
    QQSK::PropertyGroup group,
    QObject *parent) {
  return new QQStyleKitControlProperties(group, parent);
}

//  void
//      QQStyleKitControlProperties::emitChangedForAllStyleProperties(EmitFla
//      gs emitFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties32emitChangedForAllStylePropertiesE6QFlagsIN23QQStyleKitPropertyGroup8EmitFlagEE(
    QQStyleKitControlProperties *self,
    int emitFlags) {
  self->emitChangedForAllStyleProperties(
      QFlags<QQStyleKitPropertyGroup::EmitFlag>::fromInt(emitFlags));
}

//  void QQStyleKitControlProperties::forEachUsedDelegate(std::function<void
//      (QQStyleKitDelegateProperties *, QQSK::Delegate, const QString &)> f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties19forEachUsedDelegateESt8functionIFvP28QQStyleKitDelegatePropertiesN4QQSK8DelegateERK7QStringEE(
    QQStyleKitControlProperties *self,
    const std::function<void (QQStyleKitDelegateProperties *, QQSK::Delegate, const QString &)> *f) {
  self->forEachUsedDelegate(*f);
}

//  QQStyleKitStyle *QQStyleKitControlProperties::style() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK27QQStyleKitControlProperties5styleEv(
    const QQStyleKitControlProperties *self) {
  return self->style();
}

//  QQSK::Subclass QQStyleKitControlProperties::subclass() const
extern "C" Q_DECL_EXPORT
QQSK::Subclass ritual_ZNK27QQStyleKitControlProperties8subclassEv(
    const QQStyleKitControlProperties *self) {
  return self->subclass();
}

//  QQStyleKitReader *QQStyleKitControlProperties::asQQStyleKitReader() const
extern "C" Q_DECL_EXPORT
QQStyleKitReader *ritual_ZNK27QQStyleKitControlProperties18asQQStyleKitReaderEv(
    const QQStyleKitControlProperties *self) {
  return self->asQQStyleKitReader();
}

//  QQStyleKitControlState *QQStyleKitControlProperties::asQQStyleKitState()
//      const
extern "C" Q_DECL_EXPORT
QQStyleKitControlState *ritual_ZNK27QQStyleKitControlProperties17asQQStyleKitStateEv(
    const QQStyleKitControlProperties *self) {
  return self->asQQStyleKitState();
}

//  qreal QQStyleKitControlProperties::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties7spacingEv(
    const QQStyleKitControlProperties *self) {
  return self->spacing();
}

//  void QQStyleKitControlProperties::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties10setSpacingEd(
    QQStyleKitControlProperties *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  qreal QQStyleKitControlProperties::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties7paddingEv(
    const QQStyleKitControlProperties *self) {
  return self->padding();
}

//  void QQStyleKitControlProperties::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties10setPaddingEd(
    QQStyleKitControlProperties *self,
    qreal padding) {
  self->setPadding(padding);
}

//  qreal QQStyleKitControlProperties::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties11leftPaddingEv(
    const QQStyleKitControlProperties *self) {
  return self->leftPadding();
}

//  void QQStyleKitControlProperties::setLeftPadding(qreal leftPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties14setLeftPaddingEd(
    QQStyleKitControlProperties *self,
    qreal leftPadding) {
  self->setLeftPadding(leftPadding);
}

//  qreal QQStyleKitControlProperties::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties12rightPaddingEv(
    const QQStyleKitControlProperties *self) {
  return self->rightPadding();
}

//  void QQStyleKitControlProperties::setRightPadding(qreal rightPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties15setRightPaddingEd(
    QQStyleKitControlProperties *self,
    qreal rightPadding) {
  self->setRightPadding(rightPadding);
}

//  qreal QQStyleKitControlProperties::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties10topPaddingEv(
    const QQStyleKitControlProperties *self) {
  return self->topPadding();
}

//  void QQStyleKitControlProperties::setTopPadding(qreal topPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties13setTopPaddingEd(
    QQStyleKitControlProperties *self,
    qreal topPadding) {
  self->setTopPadding(topPadding);
}

//  qreal QQStyleKitControlProperties::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQStyleKitControlProperties13bottomPaddingEv(
    const QQStyleKitControlProperties *self) {
  return self->bottomPadding();
}

//  void QQStyleKitControlProperties::setBottomPadding(qreal bottomPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties16setBottomPaddingEd(
    QQStyleKitControlProperties *self,
    qreal bottomPadding) {
  self->setBottomPadding(bottomPadding);
}

//  QQuickTransition *QQStyleKitControlProperties::transition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK27QQStyleKitControlProperties10transitionEv(
    const QQStyleKitControlProperties *self) {
  return self->transition();
}

//  void QQStyleKitControlProperties::setTransition(QQuickTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties13setTransitionEP16QQuickTransition(
    QQStyleKitControlProperties *self,
    QQuickTransition *transition) {
  self->setTransition(transition);
}

//  QQStyleKitTextProperties *QQStyleKitControlProperties::text() const
extern "C" Q_DECL_EXPORT
QQStyleKitTextProperties *ritual_ZNK27QQStyleKitControlProperties4textEv(
    const QQStyleKitControlProperties *self) {
  return self->text();
}

//  QQStyleKitDelegateProperties *QQStyleKitControlProperties::background()
//      const
extern "C" Q_DECL_EXPORT
QQStyleKitDelegateProperties *ritual_ZNK27QQStyleKitControlProperties10backgroundEv(
    const QQStyleKitControlProperties *self) {
  return self->background();
}

//  QQStyleKitHandleProperties *QQStyleKitControlProperties::handle() const
extern "C" Q_DECL_EXPORT
QQStyleKitHandleProperties *ritual_ZNK27QQStyleKitControlProperties6handleEv(
    const QQStyleKitControlProperties *self) {
  return self->handle();
}

//  QQStyleKitIndicatorWithSubTypes *QQStyleKitControlProperties::indicator()
//      const
extern "C" Q_DECL_EXPORT
QQStyleKitIndicatorWithSubTypes *ritual_ZNK27QQStyleKitControlProperties9indicatorEv(
    const QQStyleKitControlProperties *self) {
  return self->indicator();
}

//  void QQStyleKitControlProperties::backgroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties17backgroundChangedEv(
    QQStyleKitControlProperties *self) {
  self->backgroundChanged();
}

//  void QQStyleKitControlProperties::handleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties13handleChangedEv(
    QQStyleKitControlProperties *self) {
  self->handleChanged();
}

//  void QQStyleKitControlProperties::indicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties16indicatorChangedEv(
    QQStyleKitControlProperties *self) {
  self->indicatorChanged();
}

//  void QQStyleKitControlProperties::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties14spacingChangedEv(
    QQStyleKitControlProperties *self) {
  self->spacingChanged();
}

//  void QQStyleKitControlProperties::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties14paddingChangedEv(
    QQStyleKitControlProperties *self) {
  self->paddingChanged();
}

//  void QQStyleKitControlProperties::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties18leftPaddingChangedEv(
    QQStyleKitControlProperties *self) {
  self->leftPaddingChanged();
}

//  void QQStyleKitControlProperties::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties19rightPaddingChangedEv(
    QQStyleKitControlProperties *self) {
  self->rightPaddingChanged();
}

//  void QQStyleKitControlProperties::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties17topPaddingChangedEv(
    QQStyleKitControlProperties *self) {
  self->topPaddingChanged();
}

//  void QQStyleKitControlProperties::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties20bottomPaddingChangedEv(
    QQStyleKitControlProperties *self) {
  self->bottomPaddingChanged();
}

//  void QQStyleKitControlProperties::transitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties17transitionChangedEv(
    QQStyleKitControlProperties *self) {
  self->transitionChanged();
}

//  void QQStyleKitControlProperties::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitControlProperties11textChangedEv(
    QQStyleKitControlProperties *self) {
  self->textChanged();
}

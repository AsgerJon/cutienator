//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qinputmethod.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qinputmethod.h>
#include <QtCore/qstring.h>
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QInputMethod::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QInputMethod10metaObjectEv(
    const QInputMethod *self) {
  return self->metaObject();
}

//  void *QInputMethod::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QInputMethod11qt_metacastEPKc(
    QInputMethod *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QInputMethod::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QInputMethod11qt_metacallEN11QMetaObject4CallEiPPv(
    QInputMethod *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QInputMethod::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputMethod2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputMethod::tr(s, c, n));
}

//  QInputMethodPrivate *QInputMethod::d_func()
extern "C" Q_DECL_EXPORT
QInputMethodPrivate *ritual_ZN12QInputMethod6d_funcEv(QInputMethod *self) {
  return self->d_func();
}

//  const QInputMethodPrivate *QInputMethod::d_func() const
extern "C" Q_DECL_EXPORT
const QInputMethodPrivate *ritual_ZNK12QInputMethod6d_funcEv(
    const QInputMethod *self) {
  return self->d_func();
}

//  QTransform QInputMethod::inputItemTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK12QInputMethod18inputItemTransformEv(
    const QInputMethod *self) {
  return new QTransform(self->inputItemTransform());
}

//  void QInputMethod::setInputItemTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod21setInputItemTransformERK10QTransform(
    QInputMethod *self,
    const QTransform *transform) {
  self->setInputItemTransform(*transform);
}

//  QRectF QInputMethod::inputItemRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QInputMethod18inputItemRectangleEv(
    const QInputMethod *self) {
  return new QRectF(self->inputItemRectangle());
}

//  void QInputMethod::setInputItemRectangle(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod21setInputItemRectangleERK6QRectF(
    QInputMethod *self,
    const QRectF *rect) {
  self->setInputItemRectangle(*rect);
}

//  QRectF QInputMethod::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QInputMethod15cursorRectangleEv(
    const QInputMethod *self) {
  return new QRectF(self->cursorRectangle());
}

//  QRectF QInputMethod::anchorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QInputMethod15anchorRectangleEv(
    const QInputMethod *self) {
  return new QRectF(self->anchorRectangle());
}

//  QRectF QInputMethod::keyboardRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QInputMethod17keyboardRectangleEv(
    const QInputMethod *self) {
  return new QRectF(self->keyboardRectangle());
}

//  QRectF QInputMethod::inputItemClipRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QInputMethod22inputItemClipRectangleEv(
    const QInputMethod *self) {
  return new QRectF(self->inputItemClipRectangle());
}

//  bool QInputMethod::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputMethod9isVisibleEv(const QInputMethod *self) {
  return self->isVisible();
}

//  void QInputMethod::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod10setVisibleEb(
    QInputMethod *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QInputMethod::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputMethod11isAnimatingEv(const QInputMethod *self) {
  return self->isAnimating();
}

//  QLocale QInputMethod::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK12QInputMethod6localeEv(const QInputMethod *self) {
  return new QLocale(self->locale());
}

//  Qt::LayoutDirection QInputMethod::inputDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK12QInputMethod14inputDirectionEv(
    const QInputMethod *self) {
  return self->inputDirection();
}

//  QVariant QInputMethod::queryFocusObject(Qt::InputMethodQuery query, const
//      QVariant &argument)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QInputMethod16queryFocusObjectEN2Qt16InputMethodQueryERK8QVariant(
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(QInputMethod::queryFocusObject(query, *argument));
}

//  void QInputMethod::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod4showEv(QInputMethod *self) {
  self->show();
}

//  void QInputMethod::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod4hideEv(QInputMethod *self) {
  self->hide();
}

//  void QInputMethod::update(Qt::InputMethodQueries queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QInputMethod *self,
    int queries) {
  self->update(QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  void QInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod5resetEv(QInputMethod *self) {
  self->reset();
}

//  void QInputMethod::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod6commitEv(QInputMethod *self) {
  self->commit();
}

//  void QInputMethod::invokeAction(Action a, int cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod12invokeActionENS_6ActionEi(
    QInputMethod *self,
    QInputMethod::Action a,
    int cursorPosition) {
  self->invokeAction(a, cursorPosition);
}

//  void QInputMethod::cursorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod22cursorRectangleChangedEv(QInputMethod *self) {
  self->cursorRectangleChanged();
}

//  void QInputMethod::anchorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod22anchorRectangleChangedEv(QInputMethod *self) {
  self->anchorRectangleChanged();
}

//  void QInputMethod::keyboardRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod24keyboardRectangleChangedEv(
    QInputMethod *self) {
  self->keyboardRectangleChanged();
}

//  void QInputMethod::inputItemClipRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod29inputItemClipRectangleChangedEv(
    QInputMethod *self) {
  self->inputItemClipRectangleChanged();
}

//  void QInputMethod::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod14visibleChangedEv(QInputMethod *self) {
  self->visibleChanged();
}

//  void QInputMethod::animatingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod16animatingChangedEv(QInputMethod *self) {
  self->animatingChanged();
}

//  void QInputMethod::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod13localeChangedEv(QInputMethod *self) {
  self->localeChanged();
}

//  void QInputMethod::inputDirectionChanged(Qt::LayoutDirection
//      newDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethod21inputDirectionChangedEN2Qt15LayoutDirectionE(
    QInputMethod *self,
    Qt::LayoutDirection newDirection) {
  self->inputDirectionChanged(newDirection);
}

//  QInputMethod::QInputMethod()
extern "C" Q_DECL_EXPORT
QInputMethod *ritual_ZN12QInputMethodC1Ev() {
  return new QInputMethod();
}

//  QInputMethod::~QInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputMethodD1Ev(QInputMethod *self) {
  delete self;
}

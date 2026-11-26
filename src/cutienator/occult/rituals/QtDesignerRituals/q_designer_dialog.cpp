//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  Only a class built on QDesignerDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDesignerDialog : QDesignerDialog {
  using QDesignerDialog::paintEvent;
};

//  const QMetaObject *QDesignerDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QDesignerDialog10metaObjectEv(
    const QDesignerDialog *self) {
  return self->metaObject();
}

//  void *QDesignerDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QDesignerDialog11qt_metacastEPKc(
    QDesignerDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerDialog::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QDesignerDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QDesignerDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerDialog::tr(s, c, n));
}

//  QDesignerDialog::QDesignerDialog(QDesignerFormWindowInterface *fw,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerDialog *ritual_ZN15QDesignerDialogC1EP28QDesignerFormWindowInterfaceP7QWidget(
    QDesignerFormWindowInterface *fw,
    QWidget *parent) {
  return new QDesignerDialog(fw, parent);
}

//  QSize QDesignerDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QDesignerDialog15minimumSizeHintEv(
    const QDesignerDialog *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDesignerDialog::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDesignerDialog10paintEventEP11QPaintEvent(
    QDesignerDialog *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  QSize QDesignerDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QDesignerDialog15minimumSizeHintEv(
    const QDesignerDialog *self) {
  return new QSize(self->QDesignerDialog::minimumSizeHint());
}

//  void QDesignerDialog::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QDesignerDialog10paintEventEP11QPaintEvent(
    QDesignerDialog *self,
    QPaintEvent *e) {
  static_cast<OwnQDesignerDialog *>(self)->OwnQDesignerDialog::paintEvent(e);
}

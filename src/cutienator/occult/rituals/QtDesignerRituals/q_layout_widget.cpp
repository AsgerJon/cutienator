//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QLayoutWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLayoutWidget : QLayoutWidget {
  using QLayoutWidget::event;
  using QLayoutWidget::paintEvent;
};

//  const QMetaObject *QLayoutWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QLayoutWidget10metaObjectEv(
    const QLayoutWidget *self) {
  return self->metaObject();
}

//  QString QLayoutWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QLayoutWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLayoutWidget::tr(s, c, n));
}

//  QLayoutWidget::QLayoutWidget(QDesignerFormWindowInterface *formWindow,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QLayoutWidget *ritual_ZN13QLayoutWidgetC1EP28QDesignerFormWindowInterfaceP7QWidget(
    QDesignerFormWindowInterface *formWindow,
    QWidget *parent) {
  return new QLayoutWidget(formWindow, parent);
}

//  int QLayoutWidget::layoutLeftMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutWidget16layoutLeftMarginEv(
    const QLayoutWidget *self) {
  return self->layoutLeftMargin();
}

//  void QLayoutWidget::setLayoutLeftMargin(int layoutMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutWidget19setLayoutLeftMarginEi(
    QLayoutWidget *self,
    int layoutMargin) {
  self->setLayoutLeftMargin(layoutMargin);
}

//  int QLayoutWidget::layoutTopMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutWidget15layoutTopMarginEv(const QLayoutWidget *self) {
  return self->layoutTopMargin();
}

//  void QLayoutWidget::setLayoutTopMargin(int layoutMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutWidget18setLayoutTopMarginEi(
    QLayoutWidget *self,
    int layoutMargin) {
  self->setLayoutTopMargin(layoutMargin);
}

//  int QLayoutWidget::layoutRightMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutWidget17layoutRightMarginEv(
    const QLayoutWidget *self) {
  return self->layoutRightMargin();
}

//  void QLayoutWidget::setLayoutRightMargin(int layoutMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutWidget20setLayoutRightMarginEi(
    QLayoutWidget *self,
    int layoutMargin) {
  self->setLayoutRightMargin(layoutMargin);
}

//  int QLayoutWidget::layoutBottomMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutWidget18layoutBottomMarginEv(
    const QLayoutWidget *self) {
  return self->layoutBottomMargin();
}

//  void QLayoutWidget::setLayoutBottomMargin(int layoutMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutWidget21setLayoutBottomMarginEi(
    QLayoutWidget *self,
    int layoutMargin) {
  self->setLayoutBottomMargin(layoutMargin);
}

//  QDesignerFormWindowInterface *QLayoutWidget::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK13QLayoutWidget10formWindowEv(
    const QLayoutWidget *self) {
  return self->formWindow();
}

//  bool QLayoutWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QLayoutWidget5eventEP6QEvent(
    QLayoutWidget *self,
    QEvent *e) {
  return self->event(e);
}

//  void QLayoutWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutWidget10paintEventEP11QPaintEvent(
    QLayoutWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  bool QLayoutWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QLayoutWidget5eventEP6QEvent(
    QLayoutWidget *self,
    QEvent *e) {
  return static_cast<OwnQLayoutWidget *>(self)->OwnQLayoutWidget::event(e);
}

//  void QLayoutWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QLayoutWidget10paintEventEP11QPaintEvent(
    QLayoutWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQLayoutWidget *>(self)->OwnQLayoutWidget::paintEvent(e);
}

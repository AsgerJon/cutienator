//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractscrollarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractscrollarea.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QAbstractScrollArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractScrollArea10metaObjectEv(
    const QAbstractScrollArea *self) {
  return self->metaObject();
}

//  QString QAbstractScrollArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractScrollArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractScrollArea::tr(s, c, n));
}

//  QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractScrollArea *ritual_ZN19QAbstractScrollAreaC1EP7QWidget(
    QWidget *parent) {
  return new QAbstractScrollArea(parent);
}

//  QAbstractScrollArea::~QAbstractScrollArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollAreaD1Ev(QAbstractScrollArea *self) {
  delete self;
}

//  Qt::ScrollBarPolicy QAbstractScrollArea::verticalScrollBarPolicy() const
extern "C" Q_DECL_EXPORT
Qt::ScrollBarPolicy ritual_ZNK19QAbstractScrollArea23verticalScrollBarPolicyEv(
    const QAbstractScrollArea *self) {
  return self->verticalScrollBarPolicy();
}

//  void QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::ScrollBarPolicy
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea26setVerticalScrollBarPolicyEN2Qt15ScrollBarPolicyE(
    QAbstractScrollArea *self,
    Qt::ScrollBarPolicy a0) {
  self->setVerticalScrollBarPolicy(a0);
}

//  QScrollBar *QAbstractScrollArea::verticalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QAbstractScrollArea17verticalScrollBarEv(
    const QAbstractScrollArea *self) {
  return self->verticalScrollBar();
}

//  void QAbstractScrollArea::setVerticalScrollBar(QScrollBar *scrollbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea20setVerticalScrollBarEP10QScrollBar(
    QAbstractScrollArea *self,
    QScrollBar *scrollbar) {
  self->setVerticalScrollBar(scrollbar);
}

//  Qt::ScrollBarPolicy QAbstractScrollArea::horizontalScrollBarPolicy()
//      const
extern "C" Q_DECL_EXPORT
Qt::ScrollBarPolicy ritual_ZNK19QAbstractScrollArea25horizontalScrollBarPolicyEv(
    const QAbstractScrollArea *self) {
  return self->horizontalScrollBarPolicy();
}

//  void
//      QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea28setHorizontalScrollBarPolicyEN2Qt15ScrollBarPolicyE(
    QAbstractScrollArea *self,
    Qt::ScrollBarPolicy a0) {
  self->setHorizontalScrollBarPolicy(a0);
}

//  QScrollBar *QAbstractScrollArea::horizontalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QAbstractScrollArea19horizontalScrollBarEv(
    const QAbstractScrollArea *self) {
  return self->horizontalScrollBar();
}

//  void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar *scrollbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea22setHorizontalScrollBarEP10QScrollBar(
    QAbstractScrollArea *self,
    QScrollBar *scrollbar) {
  self->setHorizontalScrollBar(scrollbar);
}

//  QWidget *QAbstractScrollArea::cornerWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAbstractScrollArea12cornerWidgetEv(
    const QAbstractScrollArea *self) {
  return self->cornerWidget();
}

//  void QAbstractScrollArea::setCornerWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea15setCornerWidgetEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *widget) {
  self->setCornerWidget(widget);
}

//  void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea18addScrollBarWidgetEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractScrollArea *self,
    QWidget *widget,
    int alignment) {
  self->addScrollBarWidget(
      widget,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QWidget *QAbstractScrollArea::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAbstractScrollArea8viewportEv(
    const QAbstractScrollArea *self) {
  return self->viewport();
}

//  void QAbstractScrollArea::setViewport(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea11setViewportEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *widget) {
  self->setViewport(widget);
}

//  QSize QAbstractScrollArea::maximumViewportSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea19maximumViewportSizeEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->maximumViewportSize());
}

//  QSize QAbstractScrollArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea15minimumSizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSize QAbstractScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea8sizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->sizeHint());
}

//  void QAbstractScrollArea::setupViewport(QWidget *viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea13setupViewportEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *viewport) {
  self->setupViewport(viewport);
}

//  SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy() const
extern "C" Q_DECL_EXPORT
QAbstractScrollArea::SizeAdjustPolicy ritual_ZNK19QAbstractScrollArea16sizeAdjustPolicyEv(
    const QAbstractScrollArea *self) {
  return self->sizeAdjustPolicy();
}

//  void QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea19setSizeAdjustPolicyENS_16SizeAdjustPolicyE(
    QAbstractScrollArea *self,
    QAbstractScrollArea::SizeAdjustPolicy policy) {
  self->setSizeAdjustPolicy(policy);
}

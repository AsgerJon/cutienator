//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QStackedWidgetPreviewEventFilter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStackedWidgetPreviewEventFilter : QStackedWidgetPreviewEventFilter {
  using QStackedWidgetPreviewEventFilter::gotoPage;
};

//  const QMetaObject *QStackedWidgetPreviewEventFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QStackedWidgetPreviewEventFilter10metaObjectEv(
    const QStackedWidgetPreviewEventFilter *self) {
  return self->metaObject();
}

//  QString QStackedWidgetPreviewEventFilter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QStackedWidgetPreviewEventFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedWidgetPreviewEventFilter::tr(s, c, n));
}

//  QStackedWidgetPreviewEventFilter::QStackedWidgetPreviewEventFilter(QStack
//      edWidget *parent)
extern "C" Q_DECL_EXPORT
QStackedWidgetPreviewEventFilter *ritual_ZN32QStackedWidgetPreviewEventFilterC1EP14QStackedWidget(
    QStackedWidget *parent) {
  return new QStackedWidgetPreviewEventFilter(parent);
}

//  void QStackedWidgetPreviewEventFilter::install(QStackedWidget
//      *stackedWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter7installEP14QStackedWidget(
    QStackedWidget *stackedWidget) {
  QStackedWidgetPreviewEventFilter::install(stackedWidget);
}

//  bool QStackedWidgetPreviewEventFilter::eventFilter(QObject *watched,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QStackedWidgetPreviewEventFilter11eventFilterEP7QObjectP6QEvent(
    QStackedWidgetPreviewEventFilter *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  void QStackedWidgetPreviewEventFilter::setButtonToolTipEnabled(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter23setButtonToolTipEnabledEb(
    QStackedWidgetPreviewEventFilter *self,
    bool v) {
  self->setButtonToolTipEnabled(v);
}

//  bool QStackedWidgetPreviewEventFilter::buttonToolTipEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QStackedWidgetPreviewEventFilter20buttonToolTipEnabledEv(
    const QStackedWidgetPreviewEventFilter *self) {
  return self->buttonToolTipEnabled();
}

//  void QStackedWidgetPreviewEventFilter::updateButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter13updateButtonsEv(
    QStackedWidgetPreviewEventFilter *self) {
  self->updateButtons();
}

//  void QStackedWidgetPreviewEventFilter::prevPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter8prevPageEv(
    QStackedWidgetPreviewEventFilter *self) {
  self->prevPage();
}

//  void QStackedWidgetPreviewEventFilter::nextPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter8nextPageEv(
    QStackedWidgetPreviewEventFilter *self) {
  self->nextPage();
}

//  QStackedWidget *QStackedWidgetPreviewEventFilter::stackedWidget() const
extern "C" Q_DECL_EXPORT
QStackedWidget *ritual_ZNK32QStackedWidgetPreviewEventFilter13stackedWidgetEv(
    const QStackedWidgetPreviewEventFilter *self) {
  return self->stackedWidget();
}

//  void QStackedWidgetPreviewEventFilter::gotoPage(int page)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter8gotoPageEi(
    QStackedWidgetPreviewEventFilter *self,
    int page) {
  self->gotoPage(page);
}

//  void QStackedWidgetPreviewEventFilter::updateButtonToolTip(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QStackedWidgetPreviewEventFilter19updateButtonToolTipEP7QObject(
    QStackedWidgetPreviewEventFilter *self,
    QObject *o) {
  self->updateButtonToolTip(o);
}

//  bool QStackedWidgetPreviewEventFilter::eventFilter(QObject *watched,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN32QStackedWidgetPreviewEventFilter11eventFilterEP7QObjectP6QEvent(
    QStackedWidgetPreviewEventFilter *self,
    QObject *watched,
    QEvent *event) {
  return self->QStackedWidgetPreviewEventFilter::eventFilter(watched, event);
}

//  void QStackedWidgetPreviewEventFilter::gotoPage(int page)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QStackedWidgetPreviewEventFilter8gotoPageEi(
    QStackedWidgetPreviewEventFilter *self,
    int page) {
  static_cast<OwnQStackedWidgetPreviewEventFilter *>(self)->OwnQStackedWidgetPreviewEventFilter::gotoPage(
      page);
}

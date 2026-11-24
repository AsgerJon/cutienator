//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QStackedWidgetEventFilter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStackedWidgetEventFilter : QStackedWidgetEventFilter {
  using QStackedWidgetEventFilter::gotoPage;
};

//  const QMetaObject *QStackedWidgetEventFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QStackedWidgetEventFilter10metaObjectEv(
    const QStackedWidgetEventFilter *self) {
  return self->metaObject();
}

//  QString QStackedWidgetEventFilter::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QStackedWidgetEventFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedWidgetEventFilter::tr(s, c, n));
}

//  QStackedWidgetEventFilter::QStackedWidgetEventFilter(QStackedWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QStackedWidgetEventFilter *ritual_ZN25QStackedWidgetEventFilterC1EP14QStackedWidget(
    QStackedWidget *parent) {
  return new QStackedWidgetEventFilter(parent);
}

//  void QStackedWidgetEventFilter::install(QStackedWidget *stackedWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter7installEP14QStackedWidget(
    QStackedWidget *stackedWidget) {
  QStackedWidgetEventFilter::install(stackedWidget);
}

//  QStackedWidgetEventFilter *QStackedWidgetEventFilter::eventFilterOf(const
//      QStackedWidget *stackedWidget)
extern "C" Q_DECL_EXPORT
QStackedWidgetEventFilter *ritual_ZN25QStackedWidgetEventFilter13eventFilterOfEPK14QStackedWidget(
    const QStackedWidget *stackedWidget) {
  return QStackedWidgetEventFilter::eventFilterOf(stackedWidget);
}

//  QMenu
//      *QStackedWidgetEventFilter::addStackedWidgetContextMenuActions(const
//      QStackedWidget *stackedWidget, QMenu *popup)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN25QStackedWidgetEventFilter34addStackedWidgetContextMenuActionsEPK14QStackedWidgetP5QMenu(
    const QStackedWidget *stackedWidget,
    QMenu *popup) {
  return QStackedWidgetEventFilter::addStackedWidgetContextMenuActions(
      stackedWidget,
      popup);
}

//  QMenu *QStackedWidgetEventFilter::addContextMenuActions(QMenu *popup)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN25QStackedWidgetEventFilter21addContextMenuActionsEP5QMenu(
    QStackedWidgetEventFilter *self,
    QMenu *popup) {
  return self->addContextMenuActions(popup);
}

//  void QStackedWidgetEventFilter::removeCurrentPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter17removeCurrentPageEv(
    QStackedWidgetEventFilter *self) {
  self->removeCurrentPage();
}

//  void QStackedWidgetEventFilter::addPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter7addPageEv(
    QStackedWidgetEventFilter *self) {
  self->addPage();
}

//  void QStackedWidgetEventFilter::addPageAfter()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter12addPageAfterEv(
    QStackedWidgetEventFilter *self) {
  self->addPageAfter();
}

//  void QStackedWidgetEventFilter::changeOrder()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter11changeOrderEv(
    QStackedWidgetEventFilter *self) {
  self->changeOrder();
}

//  void QStackedWidgetEventFilter::gotoPage(int page)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStackedWidgetEventFilter8gotoPageEi(
    QStackedWidgetEventFilter *self,
    int page) {
  self->gotoPage(page);
}

//  void QStackedWidgetEventFilter::gotoPage(int page)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QStackedWidgetEventFilter8gotoPageEi(
    QStackedWidgetEventFilter *self,
    int page) {
  static_cast<OwnQStackedWidgetEventFilter *>(self)->OwnQStackedWidgetEventFilter::gotoPage(
      page);
}

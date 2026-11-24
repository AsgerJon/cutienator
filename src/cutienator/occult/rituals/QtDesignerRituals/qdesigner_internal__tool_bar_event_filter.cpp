//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbar_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *qdesigner_internal::ToolBarEventFilter::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal18ToolBarEventFilter10metaObjectEv(
    const qdesigner_internal::ToolBarEventFilter *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ToolBarEventFilter::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal18ToolBarEventFilter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ToolBarEventFilter::tr(s, c, n));
}

//  QAction *qdesigner_internal::ToolBarEventFilter::createAction(QDesignerFo
//      rmWindowInterface *fw, const QString &objectName, bool separator)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN18qdesigner_internal18ToolBarEventFilter12createActionEP28QDesignerFormWindowInterfaceRK7QStringb(
    QDesignerFormWindowInterface *fw,
    const QString *objectName,
    bool separator) {
  return qdesigner_internal::ToolBarEventFilter::createAction(
      fw,
      *objectName,
      separator);
}

//  bool qdesigner_internal::ToolBarEventFilter::eventFilter(QObject
//      *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal18ToolBarEventFilter11eventFilterEP7QObjectP6QEvent(
    qdesigner_internal::ToolBarEventFilter *self,
    QObject *watched,
    QEvent *event) {
  return self->qdesigner_internal::ToolBarEventFilter::eventFilter(
      watched,
      event);
}

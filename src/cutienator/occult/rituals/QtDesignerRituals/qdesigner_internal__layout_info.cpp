//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/layoutinfo_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/layoutinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void qdesigner_internal::LayoutInfo::deleteLayout(const
//      QDesignerFormEditorInterface *core, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10LayoutInfo12deleteLayoutEPK28QDesignerFormEditorInterfaceP7QWidget(
    const QDesignerFormEditorInterface *core,
    QWidget *widget) {
  qdesigner_internal::LayoutInfo::deleteLayout(core, widget);
}

//  Type qdesigner_internal::LayoutInfo::layoutType(const
//      QDesignerFormEditorInterface *core, const QWidget *w)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutInfo::Type ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeEPK28QDesignerFormEditorInterfacePK7QWidget(
    const QDesignerFormEditorInterface *core,
    const QWidget *w) {
  return qdesigner_internal::LayoutInfo::layoutType(core, w);
}

//  Type qdesigner_internal::LayoutInfo::managedLayoutType(const
//      QDesignerFormEditorInterface *core, const QWidget *w, QLayout
//      **layout)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutInfo::Type ritual_ZN18qdesigner_internal10LayoutInfo17managedLayoutTypeEPK28QDesignerFormEditorInterfacePK7QWidgetPP7QLayout(
    const QDesignerFormEditorInterface *core,
    const QWidget *w,
    QLayout **layout) {
  return qdesigner_internal::LayoutInfo::managedLayoutType(core, w, layout);
}

//  Type qdesigner_internal::LayoutInfo::layoutType(const
//      QDesignerFormEditorInterface *core, const QLayout *layout)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutInfo::Type ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeEPK28QDesignerFormEditorInterfacePK7QLayout(
    const QDesignerFormEditorInterface *core,
    const QLayout *layout) {
  return qdesigner_internal::LayoutInfo::layoutType(core, layout);
}

//  Type qdesigner_internal::LayoutInfo::layoutType(const QString &typeName)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutInfo::Type ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeERK7QString(
    const QString *typeName) {
  return qdesigner_internal::LayoutInfo::layoutType(*typeName);
}

//  QString qdesigner_internal::LayoutInfo::layoutName(Type t)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal10LayoutInfo10layoutNameENS0_4TypeE(
    qdesigner_internal::LayoutInfo::Type t) {
  return new QString(qdesigner_internal::LayoutInfo::layoutName(t));
}

//  QWidget *qdesigner_internal::LayoutInfo::layoutParent(const
//      QDesignerFormEditorInterface *core, QLayout *layout)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal10LayoutInfo12layoutParentEPK28QDesignerFormEditorInterfaceP7QLayout(
    const QDesignerFormEditorInterface *core,
    QLayout *layout) {
  return qdesigner_internal::LayoutInfo::layoutParent(core, layout);
}

//  Type qdesigner_internal::LayoutInfo::laidoutWidgetType(const
//      QDesignerFormEditorInterface *core, QWidget *widget, bool *isManaged,
//      QLayout **layout)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutInfo::Type ritual_ZN18qdesigner_internal10LayoutInfo17laidoutWidgetTypeEPK28QDesignerFormEditorInterfaceP7QWidgetPbPP7QLayout(
    const QDesignerFormEditorInterface *core,
    QWidget *widget,
    bool *isManaged,
    QLayout **layout) {
  return qdesigner_internal::LayoutInfo::laidoutWidgetType(
      core,
      widget,
      isManaged,
      layout);
}

//  bool qdesigner_internal::LayoutInfo::isWidgetLaidout(const
//      QDesignerFormEditorInterface *core, QWidget *widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal10LayoutInfo15isWidgetLaidoutEPK28QDesignerFormEditorInterfaceP7QWidget(
    const QDesignerFormEditorInterface *core,
    QWidget *widget) {
  return qdesigner_internal::LayoutInfo::isWidgetLaidout(core, widget);
}

//  QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
//      QDesignerFormEditorInterface *core, const QWidget *widget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN18qdesigner_internal10LayoutInfo13managedLayoutEPK28QDesignerFormEditorInterfacePK7QWidget(
    const QDesignerFormEditorInterface *core,
    const QWidget *widget) {
  return qdesigner_internal::LayoutInfo::managedLayout(core, widget);
}

//  QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
//      QDesignerFormEditorInterface *core, QLayout *layout)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN18qdesigner_internal10LayoutInfo13managedLayoutEPK28QDesignerFormEditorInterfaceP7QLayout(
    const QDesignerFormEditorInterface *core,
    QLayout *layout) {
  return qdesigner_internal::LayoutInfo::managedLayout(core, layout);
}

//  QLayout *qdesigner_internal::LayoutInfo::internalLayout(const QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN18qdesigner_internal10LayoutInfo14internalLayoutEPK7QWidget(
    const QWidget *widget) {
  return qdesigner_internal::LayoutInfo::internalLayout(widget);
}

//  bool qdesigner_internal::LayoutInfo::isEmptyItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal10LayoutInfo11isEmptyItemEP11QLayoutItem(
    QLayoutItem *item) {
  return qdesigner_internal::LayoutInfo::isEmptyItem(item);
}

//  qdesigner_internal::LayoutInfo::~LayoutInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10LayoutInfoD1Ev(
    qdesigner_internal::LayoutInfo *self) {
  delete self;
}

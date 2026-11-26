//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *qdesigner_internal::QDesignerWidgetBox::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal18QDesignerWidgetBox10metaObjectEv(
    const qdesigner_internal::QDesignerWidgetBox *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerWidgetBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal18QDesignerWidgetBox11qt_metacastEPKc(
    qdesigner_internal::QDesignerWidgetBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QDesignerWidgetBox::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal18QDesignerWidgetBox11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QDesignerWidgetBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::QDesignerWidgetBox::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal18QDesignerWidgetBox2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerWidgetBox::tr(s, c, n));
}

//  LoadMode qdesigner_internal::QDesignerWidgetBox::loadMode() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerWidgetBox::LoadMode ritual_ZNK18qdesigner_internal18QDesignerWidgetBox8loadModeEv(
    const qdesigner_internal::QDesignerWidgetBox *self) {
  return self->loadMode();
}

//  void qdesigner_internal::QDesignerWidgetBox::setLoadMode(LoadMode lm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18QDesignerWidgetBox11setLoadModeENS0_8LoadModeE(
    qdesigner_internal::QDesignerWidgetBox *self,
    qdesigner_internal::QDesignerWidgetBox::LoadMode lm) {
  self->setLoadMode(lm);
}

//  bool qdesigner_internal::QDesignerWidgetBox::loadContents(const QString
//      &contents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerWidgetBox12loadContentsERK7QString(
    qdesigner_internal::QDesignerWidgetBox *self,
    const QString *contents) {
  return self->loadContents(*contents);
}

//  QIcon qdesigner_internal::QDesignerWidgetBox::iconForWidget(const QString
//      &className, const QString &category) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK18qdesigner_internal18QDesignerWidgetBox13iconForWidgetERK7QStringS3_(
    const qdesigner_internal::QDesignerWidgetBox *self,
    const QString *className,
    const QString *category) {
  return new QIcon(self->iconForWidget(*className, *category));
}

//  bool qdesigner_internal::QDesignerWidgetBox::findWidget(const
//      QDesignerWidgetBoxInterface *wbox, const QString &className, const
//      QString &category, Widget *widgetData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerWidgetBox10findWidgetEPK27QDesignerWidgetBoxInterfaceRK7QStringS6_PNS1_6WidgetE(
    const QDesignerWidgetBoxInterface *wbox,
    const QString *className,
    const QString *category,
    QDesignerWidgetBoxInterface::Widget *widgetData) {
  return qdesigner_internal::QDesignerWidgetBox::findWidget(
      wbox,
      *className,
      *category,
      widgetData);
}

//  DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const QString
//      &name, const QString &xml, bool insertFakeTopLevel, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZN18qdesigner_internal18QDesignerWidgetBox7xmlToUiERK7QStringS3_bPS1_(
    const QString *name,
    const QString *xml,
    bool insertFakeTopLevel,
    QString *errorMessage) {
  return qdesigner_internal::QDesignerWidgetBox::xmlToUi(
      *name,
      *xml,
      insertFakeTopLevel,
      errorMessage);
}

//  DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const QString
//      &name, const QString &xml, bool insertFakeTopLevel)
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZN18qdesigner_internal18QDesignerWidgetBox7xmlToUiERK7QStringS3_b(
    const QString *name,
    const QString *xml,
    bool insertFakeTopLevel) {
  return qdesigner_internal::QDesignerWidgetBox::xmlToUi(
      *name,
      *xml,
      insertFakeTopLevel);
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QDesignerCustomWidgetData::QDesignerCustomWidgetData(const QString
//      &pluginPath)
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData *ritual_ZN25QDesignerCustomWidgetDataC1ERK7QString(
    const QString *pluginPath) {
  return new QDesignerCustomWidgetData(*pluginPath);
}

//  ParseResult QDesignerCustomWidgetData::parseXml(const QString &xml, const
//      QString &name, QString *errorMessage)
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData::ParseResult ritual_ZN25QDesignerCustomWidgetData8parseXmlERK7QStringS2_PS0_(
    QDesignerCustomWidgetData *self,
    const QString *xml,
    const QString *name,
    QString *errorMessage) {
  return self->parseXml(*xml, *name, errorMessage);
}

//  QDesignerCustomWidgetData::QDesignerCustomWidgetData(const
//      QDesignerCustomWidgetData &a0)
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData *ritual_ZN25QDesignerCustomWidgetDataC1ERKS_(
    const QDesignerCustomWidgetData *a0) {
  return new QDesignerCustomWidgetData(*a0);
}

//  QDesignerCustomWidgetData &QDesignerCustomWidgetData::operator=(const
//      QDesignerCustomWidgetData &a0)
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData *ritual_ZN25QDesignerCustomWidgetDataaSERKS_(
    QDesignerCustomWidgetData *self,
    const QDesignerCustomWidgetData *a0) {
  return &(self->operator=(*a0));
}

//  QDesignerCustomWidgetData::~QDesignerCustomWidgetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDesignerCustomWidgetDataD1Ev(
    QDesignerCustomWidgetData *self) {
  delete self;
}

//  bool QDesignerCustomWidgetData::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QDesignerCustomWidgetData6isNullEv(
    const QDesignerCustomWidgetData *self) {
  return self->isNull();
}

//  QString QDesignerCustomWidgetData::pluginPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData10pluginPathEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->pluginPath());
}

//  QString QDesignerCustomWidgetData::xmlClassName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData12xmlClassNameEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->xmlClassName());
}

//  QString QDesignerCustomWidgetData::xmlLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData11xmlLanguageEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->xmlLanguage());
}

//  QString QDesignerCustomWidgetData::xmlAddPageMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData16xmlAddPageMethodEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->xmlAddPageMethod());
}

//  QString QDesignerCustomWidgetData::xmlExtends() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData10xmlExtendsEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->xmlExtends());
}

//  QString QDesignerCustomWidgetData::xmlDisplayName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData14xmlDisplayNameEv(
    const QDesignerCustomWidgetData *self) {
  return new QString(self->xmlDisplayName());
}

//  bool QDesignerCustomWidgetData::xmlStringPropertyType(const QString
//      &name, StringPropertyType *type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QDesignerCustomWidgetData21xmlStringPropertyTypeERK7QStringPSt4pairIN18qdesigner_internal26TextPropertyValidationModeEbE(
    const QDesignerCustomWidgetData *self,
    const QString *name,
    QDesignerCustomWidgetData::StringPropertyType *type) {
  return self->xmlStringPropertyType(*name, type);
}

//  QString QDesignerCustomWidgetData::propertyToolTip(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDesignerCustomWidgetData15propertyToolTipERK7QString(
    const QDesignerCustomWidgetData *self,
    const QString *name) {
  return new QString(self->propertyToolTip(*name));
}

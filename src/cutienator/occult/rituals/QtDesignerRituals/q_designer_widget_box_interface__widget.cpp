//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractwidgetbox.h>
#include <QtCore/qstring.h>

//  QDesignerWidgetBoxInterface::Widget::Widget(const QString &aname, const
//      QString &xml, const QString &icon_name, Type atype)
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Widget *ritual_ZN27QDesignerWidgetBoxInterface6WidgetC1ERK7QStringS3_S3_NS0_4TypeE(
    const QString *aname,
    const QString *xml,
    const QString *icon_name,
    QDesignerWidgetBoxInterface::Widget::Type atype) {
  return new QDesignerWidgetBoxInterface::Widget(
      *aname,
      *xml,
      *icon_name,
      atype);
}

//  QDesignerWidgetBoxInterface::Widget::~Widget()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface6WidgetD1Ev(
    QDesignerWidgetBoxInterface::Widget *self) {
  delete self;
}

//  QDesignerWidgetBoxInterface::Widget::Widget(const Widget &w)
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Widget *ritual_ZN27QDesignerWidgetBoxInterface6WidgetC1ERKS0_(
    const QDesignerWidgetBoxInterface::Widget *w) {
  return new QDesignerWidgetBoxInterface::Widget(*w);
}

//  QString QDesignerWidgetBoxInterface::Widget::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerWidgetBoxInterface6Widget4nameEv(
    const QDesignerWidgetBoxInterface::Widget *self) {
  return new QString(self->name());
}

//  void QDesignerWidgetBoxInterface::Widget::setName(const QString &aname)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface6Widget7setNameERK7QString(
    QDesignerWidgetBoxInterface::Widget *self,
    const QString *aname) {
  self->setName(*aname);
}

//  QString QDesignerWidgetBoxInterface::Widget::domXml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerWidgetBoxInterface6Widget6domXmlEv(
    const QDesignerWidgetBoxInterface::Widget *self) {
  return new QString(self->domXml());
}

//  void QDesignerWidgetBoxInterface::Widget::setDomXml(const QString &xml)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface6Widget9setDomXmlERK7QString(
    QDesignerWidgetBoxInterface::Widget *self,
    const QString *xml) {
  self->setDomXml(*xml);
}

//  QString QDesignerWidgetBoxInterface::Widget::iconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerWidgetBoxInterface6Widget8iconNameEv(
    const QDesignerWidgetBoxInterface::Widget *self) {
  return new QString(self->iconName());
}

//  void QDesignerWidgetBoxInterface::Widget::setIconName(const QString
//      &icon_name)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface6Widget11setIconNameERK7QString(
    QDesignerWidgetBoxInterface::Widget *self,
    const QString *icon_name) {
  self->setIconName(*icon_name);
}

//  Type QDesignerWidgetBoxInterface::Widget::type() const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Widget::Type ritual_ZNK27QDesignerWidgetBoxInterface6Widget4typeEv(
    const QDesignerWidgetBoxInterface::Widget *self) {
  return self->type();
}

//  void QDesignerWidgetBoxInterface::Widget::setType(Type atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface6Widget7setTypeENS0_4TypeE(
    QDesignerWidgetBoxInterface::Widget *self,
    QDesignerWidgetBoxInterface::Widget::Type atype) {
  self->setType(atype);
}

//  bool QDesignerWidgetBoxInterface::Widget::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDesignerWidgetBoxInterface6Widget6isNullEv(
    const QDesignerWidgetBoxInterface::Widget *self) {
  return self->isNull();
}

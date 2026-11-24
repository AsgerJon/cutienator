//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractwidgetbox.h>
#include <QtCore/qstring.h>

//  QDesignerWidgetBoxInterface::Category::Category(const QString &aname,
//      Type atype)
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Category *ritual_ZN27QDesignerWidgetBoxInterface8CategoryC1ERK7QStringNS0_4TypeE(
    const QString *aname,
    QDesignerWidgetBoxInterface::Category::Type atype) {
  return new QDesignerWidgetBoxInterface::Category(*aname, atype);
}

//  QString QDesignerWidgetBoxInterface::Category::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerWidgetBoxInterface8Category4nameEv(
    const QDesignerWidgetBoxInterface::Category *self) {
  return new QString(self->name());
}

//  void QDesignerWidgetBoxInterface::Category::setName(const QString &aname)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface8Category7setNameERK7QString(
    QDesignerWidgetBoxInterface::Category *self,
    const QString *aname) {
  self->setName(*aname);
}

//  int QDesignerWidgetBoxInterface::Category::widgetCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDesignerWidgetBoxInterface8Category11widgetCountEv(
    const QDesignerWidgetBoxInterface::Category *self) {
  return self->widgetCount();
}

//  Widget QDesignerWidgetBoxInterface::Category::widget(int idx) const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Widget *ritual_ZNK27QDesignerWidgetBoxInterface8Category6widgetEi(
    const QDesignerWidgetBoxInterface::Category *self,
    int idx) {
  return new QDesignerWidgetBoxInterface::Widget(self->widget(idx));
}

//  void QDesignerWidgetBoxInterface::Category::removeWidget(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface8Category12removeWidgetEi(
    QDesignerWidgetBoxInterface::Category *self,
    int idx) {
  self->removeWidget(idx);
}

//  void QDesignerWidgetBoxInterface::Category::addWidget(const Widget
//      &awidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface8Category9addWidgetERKNS_6WidgetE(
    QDesignerWidgetBoxInterface::Category *self,
    const QDesignerWidgetBoxInterface::Widget *awidget) {
  self->addWidget(*awidget);
}

//  Type QDesignerWidgetBoxInterface::Category::type() const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Category::Type ritual_ZNK27QDesignerWidgetBoxInterface8Category4typeEv(
    const QDesignerWidgetBoxInterface::Category *self) {
  return self->type();
}

//  void QDesignerWidgetBoxInterface::Category::setType(Type atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface8Category7setTypeENS0_4TypeE(
    QDesignerWidgetBoxInterface::Category *self,
    QDesignerWidgetBoxInterface::Category::Type atype) {
  self->setType(atype);
}

//  bool QDesignerWidgetBoxInterface::Category::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDesignerWidgetBoxInterface8Category6isNullEv(
    const QDesignerWidgetBoxInterface::Category *self) {
  return self->isNull();
}

//  QDesignerWidgetBoxInterface::Category::~Category()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface8CategoryD1Ev(
    QDesignerWidgetBoxInterface::Category *self) {
  delete self;
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdockwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdockwidget.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QDockWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QDockWidget10metaObjectEv(
    const QDockWidget *self) {
  return self->metaObject();
}

//  QString QDockWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QDockWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDockWidget::tr(s, c, n));
}

//  QDockWidget::QDockWidget(const QString &title, QWidget *parent,
//      Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN11QDockWidgetC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *title,
    QWidget *parent,
    int flags) {
  return new QDockWidget(
      *title,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDockWidget::QDockWidget(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN11QDockWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QDockWidget(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDockWidget::~QDockWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidgetD1Ev(QDockWidget *self) {
  delete self;
}

//  QWidget *QDockWidget::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QDockWidget6widgetEv(const QDockWidget *self) {
  return self->widget();
}

//  void QDockWidget::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget9setWidgetEP7QWidget(
    QDockWidget *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  void QDockWidget::setFeatures(DockWidgetFeatures features)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget11setFeaturesE6QFlagsINS_17DockWidgetFeatureEE(
    QDockWidget *self,
    int features) {
  self->setFeatures(
      QFlags<QDockWidget::DockWidgetFeature>::fromInt(features));
}

//  DockWidgetFeatures QDockWidget::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDockWidget8featuresEv(const QDockWidget *self) {
  return static_cast<int>(self->features().toInt());
}

//  void QDockWidget::setFloating(bool floating)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget11setFloatingEb(
    QDockWidget *self,
    bool floating) {
  self->setFloating(floating);
}

//  bool QDockWidget::isFloating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDockWidget10isFloatingEv(const QDockWidget *self) {
  return self->isFloating();
}

//  void QDockWidget::setAllowedAreas(Qt::DockWidgetAreas areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget15setAllowedAreasE6QFlagsIN2Qt14DockWidgetAreaEE(
    QDockWidget *self,
    int areas) {
  self->setAllowedAreas(QFlags<Qt::DockWidgetArea>::fromInt(areas));
}

//  Qt::DockWidgetAreas QDockWidget::allowedAreas() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDockWidget12allowedAreasEv(const QDockWidget *self) {
  return static_cast<int>(self->allowedAreas().toInt());
}

//  void QDockWidget::setTitleBarWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget17setTitleBarWidgetEP7QWidget(
    QDockWidget *self,
    QWidget *widget) {
  self->setTitleBarWidget(widget);
}

//  QWidget *QDockWidget::titleBarWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QDockWidget14titleBarWidgetEv(const QDockWidget *self) {
  return self->titleBarWidget();
}

//  void QDockWidget::setDockLocation(Qt::DockWidgetArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget15setDockLocationEN2Qt14DockWidgetAreaE(
    QDockWidget *self,
    Qt::DockWidgetArea area) {
  self->setDockLocation(area);
}

//  Qt::DockWidgetArea QDockWidget::dockLocation() const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QDockWidget12dockLocationEv(
    const QDockWidget *self) {
  return self->dockLocation();
}

//  bool QDockWidget::isAreaAllowed(Qt::DockWidgetArea area) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDockWidget13isAreaAllowedEN2Qt14DockWidgetAreaE(
    const QDockWidget *self,
    Qt::DockWidgetArea area) {
  return self->isAreaAllowed(area);
}

//  QAction *QDockWidget::toggleViewAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK11QDockWidget16toggleViewActionEv(
    const QDockWidget *self) {
  return self->toggleViewAction();
}

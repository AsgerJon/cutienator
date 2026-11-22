//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwidgetaction.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwidgetaction.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QWidgetAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWidgetAction10metaObjectEv(
    const QWidgetAction *self) {
  return self->metaObject();
}

//  QString QWidgetAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QWidgetAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWidgetAction::tr(s, c, n));
}

//  QWidgetAction::QWidgetAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QWidgetAction *ritual_ZN13QWidgetActionC1EP7QObject(QObject *parent) {
  return new QWidgetAction(parent);
}

//  QWidgetAction::~QWidgetAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetActionD1Ev(QWidgetAction *self) {
  delete self;
}

//  void QWidgetAction::setDefaultWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetAction16setDefaultWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *w) {
  self->setDefaultWidget(w);
}

//  QWidget *QWidgetAction::defaultWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QWidgetAction13defaultWidgetEv(
    const QWidgetAction *self) {
  return self->defaultWidget();
}

//  QWidget *QWidgetAction::requestWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN13QWidgetAction13requestWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *parent) {
  return self->requestWidget(parent);
}

//  void QWidgetAction::releaseWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetAction13releaseWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *widget) {
  self->releaseWidget(widget);
}

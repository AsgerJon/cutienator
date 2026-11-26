//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpcontentwidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpcontentwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QHelpContentWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QHelpContentWidget10metaObjectEv(
    const QHelpContentWidget *self) {
  return self->metaObject();
}

//  void *QHelpContentWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QHelpContentWidget11qt_metacastEPKc(
    QHelpContentWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpContentWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QHelpContentWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpContentWidget::tr(s, c, n));
}

//  QModelIndex QHelpContentWidget::indexOf(const QUrl &link)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN18QHelpContentWidget7indexOfERK4QUrl(
    QHelpContentWidget *self,
    const QUrl *link) {
  return new QModelIndex(self->indexOf(*link));
}

//  void QHelpContentWidget::linkActivated(const QUrl &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHelpContentWidget13linkActivatedERK4QUrl(
    QHelpContentWidget *self,
    const QUrl *link) {
  self->linkActivated(*link);
}

//  void QHelpContentWidget::showLink(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHelpContentWidget8showLinkERK11QModelIndex(
    QHelpContentWidget *self,
    const QModelIndex *index) {
  self->showLink(*index);
}

//  bool QHelpContentWidget::searchContentItem(QHelpContentModel *model,
//      const QModelIndex &parent, const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QHelpContentWidget17searchContentItemEP17QHelpContentModelRK11QModelIndexRK7QString(
    QHelpContentWidget *self,
    QHelpContentModel *model,
    const QModelIndex *parent,
    const QString *path) {
  return self->searchContentItem(model, *parent, *path);
}

//  QHelpContentWidget::QHelpContentWidget()
extern "C" Q_DECL_EXPORT
QHelpContentWidget *ritual_ZN18QHelpContentWidgetC1Ev() {
  return new QHelpContentWidget();
}

#endif  // QT_CONFIG(fullqthelp)

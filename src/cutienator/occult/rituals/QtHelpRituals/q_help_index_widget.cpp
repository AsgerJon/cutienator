//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpindexwidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpindexwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtHelp/qhelplink.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QHelpIndexWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QHelpIndexWidget10metaObjectEv(
    const QHelpIndexWidget *self) {
  return self->metaObject();
}

//  void *QHelpIndexWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QHelpIndexWidget11qt_metacastEPKc(
    QHelpIndexWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpIndexWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QHelpIndexWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpIndexWidget::tr(s, c, n));
}

#if QT_DEPRECATED_SINCE(5, 15)
//  void QHelpIndexWidget::linkActivated(const QUrl &link, const QString
//      &keyword)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget13linkActivatedERK4QUrlRK7QString(
    QHelpIndexWidget *self,
    const QUrl *link,
    const QString *keyword) {
  self->linkActivated(*link, *keyword);
}
#endif  // QT_DEPRECATED_SINCE(5, 15)

//  void QHelpIndexWidget::documentActivated(const QHelpLink &document, const
//      QString &keyword)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget17documentActivatedERK9QHelpLinkRK7QString(
    QHelpIndexWidget *self,
    const QHelpLink *document,
    const QString *keyword) {
  self->documentActivated(*document, *keyword);
}

//  void QHelpIndexWidget::documentsActivated(const QList<QHelpLink>
//      &documents, const QString &keyword)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget18documentsActivatedERK5QListI9QHelpLinkERK7QString(
    QHelpIndexWidget *self,
    const QList<QHelpLink> *documents,
    const QString *keyword) {
  self->documentsActivated(*documents, *keyword);
}

//  void QHelpIndexWidget::filterIndices(const QString &filter, const QString
//      &wildcard)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget13filterIndicesERK7QStringS2_(
    QHelpIndexWidget *self,
    const QString *filter,
    const QString *wildcard) {
  self->filterIndices(*filter, *wildcard);
}

//  void QHelpIndexWidget::activateCurrentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget19activateCurrentItemEv(
    QHelpIndexWidget *self) {
  self->activateCurrentItem();
}

//  void QHelpIndexWidget::showLink(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpIndexWidget8showLinkERK11QModelIndex(
    QHelpIndexWidget *self,
    const QModelIndex *index) {
  self->showLink(*index);
}

//  QHelpIndexWidget::QHelpIndexWidget()
extern "C" Q_DECL_EXPORT
QHelpIndexWidget *ritual_ZN16QHelpIndexWidgetC1Ev() {
  return new QHelpIndexWidget();
}

#endif  // QT_CONFIG(fullqthelp)

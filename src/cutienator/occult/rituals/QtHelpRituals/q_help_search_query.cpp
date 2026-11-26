//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchengine.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  the config header of QtTools is included before the first #if,
//  as QT_CONFIG(fullqthelp) is defined there. Kept as it is when
//  the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#if QT_DEPRECATED_SINCE(6, 7)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpsearchengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QHelpSearchQuery::QHelpSearchQuery()
extern "C" Q_DECL_EXPORT
QHelpSearchQuery *ritual_ZN16QHelpSearchQueryC1Ev() {
  return new QHelpSearchQuery();
}

//  QHelpSearchQuery::QHelpSearchQuery(FieldName field, const QStringList
//      &wordList_)
extern "C" Q_DECL_EXPORT
QHelpSearchQuery *ritual_ZN16QHelpSearchQueryC1ENS_9FieldNameERK5QListI7QStringE(
    QHelpSearchQuery::FieldName field,
    const QList<QString> *wordList_) {
  return new QHelpSearchQuery(field, *wordList_);
}

//  QHelpSearchQuery::~QHelpSearchQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpSearchQueryD1Ev(QHelpSearchQuery *self) {
  delete self;
}

//  QList<QHelpSearchQuery>::QList()
extern "C" Q_DECL_EXPORT
QList<QHelpSearchQuery> *ritual_list_make_QHelpSearchQuery() {
  return new QList<QHelpSearchQuery>();
}

//  void QList<QHelpSearchQuery>::append(const QHelpSearchQuery &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHelpSearchQuery(
    QList<QHelpSearchQuery> *self,
    const QHelpSearchQuery *element) {
  self->append(*element);
}

//  qsizetype QList<QHelpSearchQuery>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHelpSearchQuery(
    const QList<QHelpSearchQuery> *self) {
  return self->size();
}

//  const QHelpSearchQuery &QList<QHelpSearchQuery>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHelpSearchQuery *ritual_list_at_QHelpSearchQuery(
    const QList<QHelpSearchQuery> *self,
    long long index) {
  return new QHelpSearchQuery(self->at(index));
}

//  QList<QHelpSearchQuery>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHelpSearchQuery(QList<QHelpSearchQuery> *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 7)
#endif  // QT_CONFIG(fullqthelp)

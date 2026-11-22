//  Written by hand: the rituals of Qt's QStringList, its list of text.
//  Text is no class the dev tooling writes a cute class for, so no
//  ritual file of a class holds these, as 'q_url.cpp' holds the rituals
//  of the list of QUrl.
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>

//  QList<QString>::QList()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_list_make_QString() {
  return new QList<QString>();
}

//  void QList<QString>::append(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QString(QList<QString> *self, const QString *element) {
  self->append(*element);
}

//  qsizetype QList<QString>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QString(const QList<QString> *self) {
  return self->size();
}

//  const QString &QList<QString>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QString *ritual_list_at_QString(
    const QList<QString> *self,
    long long index) {
  return new QString(self->at(index));
}

//  QList<QString>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QString(QList<QString> *self) {
  delete self;
}

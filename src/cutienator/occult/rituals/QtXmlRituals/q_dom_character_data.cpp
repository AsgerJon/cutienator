//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomCharacterData::QDomCharacterData()
extern "C" Q_DECL_EXPORT
QDomCharacterData *ritual_ZN17QDomCharacterDataC1Ev() {
  return new QDomCharacterData();
}

//  QDomCharacterData::QDomCharacterData(const QDomCharacterData
//      &characterData)
extern "C" Q_DECL_EXPORT
QDomCharacterData *ritual_ZN17QDomCharacterDataC1ERKS_(
    const QDomCharacterData *characterData) {
  return new QDomCharacterData(*characterData);
}

//  QString QDomCharacterData::substringData(unsigned long offset, unsigned
//      long count)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDomCharacterData13substringDataEmm(
    QDomCharacterData *self,
    unsigned long offset,
    unsigned long count) {
  return new QString(self->substringData(offset, count));
}

//  void QDomCharacterData::appendData(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterData10appendDataERK7QString(
    QDomCharacterData *self,
    const QString *arg) {
  self->appendData(*arg);
}

//  void QDomCharacterData::insertData(unsigned long offset, const QString
//      &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterData10insertDataEmRK7QString(
    QDomCharacterData *self,
    unsigned long offset,
    const QString *arg) {
  self->insertData(offset, *arg);
}

//  void QDomCharacterData::deleteData(unsigned long offset, unsigned long
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterData10deleteDataEmm(
    QDomCharacterData *self,
    unsigned long offset,
    unsigned long count) {
  self->deleteData(offset, count);
}

//  void QDomCharacterData::replaceData(unsigned long offset, unsigned long
//      count, const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterData11replaceDataEmmRK7QString(
    QDomCharacterData *self,
    unsigned long offset,
    unsigned long count,
    const QString *arg) {
  self->replaceData(offset, count, *arg);
}

//  int QDomCharacterData::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDomCharacterData6lengthEv(const QDomCharacterData *self) {
  return self->length();
}

//  QString QDomCharacterData::data() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDomCharacterData4dataEv(
    const QDomCharacterData *self) {
  return new QString(self->data());
}

//  void QDomCharacterData::setData(const QString &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterData7setDataERK7QString(
    QDomCharacterData *self,
    const QString *data) {
  self->setData(*data);
}

//  QDomNode::NodeType QDomCharacterData::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK17QDomCharacterData8nodeTypeEv(
    const QDomCharacterData *self) {
  return self->nodeType();
}

//  QDomCharacterData::QDomCharacterData(QDomCharacterDataPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomCharacterData *ritual_ZN17QDomCharacterDataC1EP24QDomCharacterDataPrivate(
    QDomCharacterDataPrivate *a0) {
  return new QDomCharacterData(a0);
}

//  QDomCharacterData::~QDomCharacterData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDomCharacterDataD1Ev(QDomCharacterData *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)

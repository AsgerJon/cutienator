//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcandbcfileparser.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcandbcfileparser.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtSerialBus/qcanuniqueiddescription.h>
#include <QtCore/qlist.h>
#include <QtSerialBus/QCanDbcFileParser>

//  QCanDbcFileParser::QCanDbcFileParser()
extern "C" Q_DECL_EXPORT
QCanDbcFileParser *ritual_ZN17QCanDbcFileParserC1Ev() {
  return new QCanDbcFileParser();
}

//  QCanDbcFileParser::~QCanDbcFileParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCanDbcFileParserD1Ev(QCanDbcFileParser *self) {
  delete self;
}

//  bool QCanDbcFileParser::parse(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCanDbcFileParser5parseERK7QString(
    QCanDbcFileParser *self,
    const QString *fileName) {
  return self->parse(*fileName);
}

//  bool QCanDbcFileParser::parse(const QStringList &fileNames)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCanDbcFileParser5parseERK5QListI7QStringE(
    QCanDbcFileParser *self,
    const QList<QString> *fileNames) {
  return self->parse(*fileNames);
}

//  bool QCanDbcFileParser::parseData(QStringView data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCanDbcFileParser9parseDataE11QStringView(
    QCanDbcFileParser *self,
    const QString *data) {
  return self->parseData(QStringView(*data));
}

//  QList<QCanMessageDescription> QCanDbcFileParser::messageDescriptions()
//      const
extern "C" Q_DECL_EXPORT
QList<QCanMessageDescription> *ritual_ZNK17QCanDbcFileParser19messageDescriptionsEv(
    const QCanDbcFileParser *self) {
  return new QList<QCanMessageDescription>(self->messageDescriptions());
}

//  MessageValueDescriptions QCanDbcFileParser::messageValueDescriptions()
//      const
extern "C" Q_DECL_EXPORT
QCanDbcFileParser::MessageValueDescriptions *ritual_ZNK17QCanDbcFileParser24messageValueDescriptionsEv(
    const QCanDbcFileParser *self) {
  return new QCanDbcFileParser::MessageValueDescriptions(
      self->messageValueDescriptions());
}

//  Error QCanDbcFileParser::error() const
extern "C" Q_DECL_EXPORT
QCanDbcFileParser::Error ritual_ZNK17QCanDbcFileParser5errorEv(
    const QCanDbcFileParser *self) {
  return self->error();
}

//  QString QCanDbcFileParser::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanDbcFileParser11errorStringEv(
    const QCanDbcFileParser *self) {
  return new QString(self->errorString());
}

//  QStringList QCanDbcFileParser::warnings() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QCanDbcFileParser8warningsEv(
    const QCanDbcFileParser *self) {
  return new QList<QString>(self->warnings());
}

//  QCanUniqueIdDescription QCanDbcFileParser::uniqueIdDescription()
extern "C" Q_DECL_EXPORT
QCanUniqueIdDescription *ritual_ZN17QCanDbcFileParser19uniqueIdDescriptionEv() {
  return new QCanUniqueIdDescription(
      QCanDbcFileParser::uniqueIdDescription());
}

//  a QCanDbcFileParser::MessageValueDescriptions a ritual of
//      QCanDbcFileParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCanDbcFileParser__QCanDbcFileParser_MessageValueDescriptions(
    QCanDbcFileParser::MessageValueDescriptions *self) {
  delete self;
}

package io.pivotal.training.cna.employeesapi;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Entity
public class Employee {

    @Id @GeneratedValue (strategy = GenerationType.AUTO)
    private Long id;
    private String name;
    private String office;
    private Integer deskNum;
}
